{ pkgs }:
{
  packages = [
    pkgs.deadnix
    pkgs.nixfmt
    pkgs.statix
  ];
  hooks = [
    {
      id = "nix-flake-check";
      entry = "nix flake check";
      pass_filenames = false;
      types = [ "nix" ];
    }
    {
      id = "nixfmt";
      entry = "nixfmt";
      types = [ "nix" ];
    }
    {
      id = "statix";
      entry = "statix check";
      pass_filenames = false;
      types = [ "nix" ];
    }
    {
      id = "deadnix";
      entry = "deadnix --fail";
      types = [ "nix" ];
    }
  ];
}
