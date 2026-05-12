_: {
  packages = [ ];
  hooks = [
    {
      id = "ruff-check";
      entry = "ruff check";
      types = [ "python" ];
    }
    {
      id = "ruff-format";
      entry = "ruff format";
      types = [ "python" ];
    }
    {
      id = "ty-check";
      entry = "ty check";
      pass_filenames = false;
      types = [ "python" ];
    }
    {
      id = "pytest-unit";
      name = "pytest unit tests";
      entry = "pytest -m unit_test";
      pass_filenames = false;
      types = [ "python" ];
    }
    {
      id = "pytest-contract";
      name = "pytest contract tests";
      entry = "pytest -m contract_test";
      pass_filenames = false;
      types = [ "python" ];
    }
  ];
}
