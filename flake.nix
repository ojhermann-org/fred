{
  description = "A Python library for the FRED API";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs =
    { nixpkgs, ... }:
    let
      systems = [
        "x86_64-linux"
        "aarch64-linux"
        "x86_64-darwin"
        "aarch64-darwin"
      ];
      forAllSystems = nixpkgs.lib.genAttrs systems;
      codeQualityTools =
        pkgs:
        let
          dir = ./nix/code-quality-tools;
          files = nixpkgs.lib.filesystem.listFilesRecursive dir;
          nixFiles = builtins.filter (f: nixpkgs.lib.hasSuffix ".nix" f) files;
        in
        builtins.concatMap (f: (import f { inherit pkgs; }).packages) nixFiles;
    in
    {
      devShells = forAllSystems (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            config.allowUnfree = true;
          };
        in
        {
          default = pkgs.mkShell {
            packages = [
              pkgs.bash
              pkgs.claude-code
              pkgs.git
              pkgs.helix
              pkgs.opentofu
              pkgs.prek
              pkgs.taplo
              pkgs.tombi
              pkgs.tree
              pkgs.uv
              pkgs.watchexec
              pkgs.zellij
            ]
            ++ codeQualityTools pkgs;
            shellHook = ''
              if [ -d .git ] && [ ! -f .git/hooks/pre-commit ]; then
                prek install >/dev/null 2>&1 || true
              fi
            '';
          };
        }
      );
      packages = forAllSystems (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            config.allowUnfree = true;
          };
        in
        {
          prek-toml = import ./nix/prek-toml.nix { inherit pkgs; };
        }
      );
      apps = forAllSystems (
        system:
        let
          pkgs = import nixpkgs {
            inherit system;
            config.allowUnfree = true;
          };
          prekToml = import ./nix/prek-toml.nix { inherit pkgs; };
        in
        {
          sync-prek = {
            type = "app";
            program = toString (
              pkgs.writeShellScript "sync-prek" ''
                set -euo pipefail
                repo_root="$(git rev-parse --show-toplevel)"
                install -m 644 ${prekToml} "$repo_root/prek.toml"
                echo "Wrote $repo_root/prek.toml"
              ''
            );
          };
        }
      );
    };
}
