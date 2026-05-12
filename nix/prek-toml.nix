{ pkgs }:
let
  inherit (pkgs) lib;

  toolsDir = ./code-quality-tools;
  toolFiles = builtins.filter (f: lib.hasSuffix ".nix" f) (
    lib.filesystem.listFilesRecursive toolsDir
  );
  aggregatedHooks = builtins.concatMap (f: (import f { inherit pkgs; }).hooks) toolFiles;

  builtinHookIds = [
    "no-commit-to-branch"
    "trailing-whitespace"
    "end-of-file-fixer"
    "check-merge-conflict"
    "check-toml"
    "check-yaml"
    "check-json"
    "check-xml"
    "check-added-large-files"
    "check-case-conflict"
    "detect-private-key"
  ];

  withDefaults =
    h:
    {
      name = h.id;
      language = "system";
    }
    // h;

  driftCheckHook = {
    id = "prek-toml-up-to-date";
    entry = "sh -c 'nix run .#sync-prek && git diff --exit-code prek.toml'";
    pass_filenames = false;
    files = "^(prek\\.toml|nix/code-quality-tools/.*\\.nix|flake\\.nix|nix/prek-toml\\.nix)$";
  };

  config = {
    default_install_hook_types = [
      "pre-commit"
      "pre-push"
    ];
    repos = [
      {
        repo = "builtin";
        hooks = map (id: { inherit id; }) builtinHookIds;
      }
      {
        repo = "local";
        hooks = map withDefaults (aggregatedHooks ++ [ driftCheckHook ]);
      }
    ];
  };

  tomlFormat = pkgs.formats.toml { };
in
tomlFormat.generate "prek.toml" config
