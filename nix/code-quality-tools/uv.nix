_: {
  packages = [ ];
  hooks = [
    {
      id = "uv-sync";
      entry = "uv sync";
      pass_filenames = false;
      stages = [ "pre-push" ];
    }
  ];
}
