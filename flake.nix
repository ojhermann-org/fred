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
              pkgs.awscli2
              pkgs.bash
              pkgs.claude-code
              pkgs.deadnix
              pkgs.git
              pkgs.helix
              pkgs.nixfmt
              pkgs.opentofu
              pkgs.prek
              pkgs.statix
              pkgs.taplo
              pkgs.tombi
              pkgs.tree
              pkgs.uv
              pkgs.watchexec
              pkgs.zellij
            ];
          };
        }
      );
    };
}
