_: {
  packages = [ ];
  hooks = [
    {
      id = "prek-validate-config";
      name = "prek validate-config";
      entry = "prek validate-config";
      pass_filenames = false;
      files = "prek\\.toml$";
    }
  ];
}
