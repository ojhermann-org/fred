import pytest

from fred.request.enum.endpoint import Base, combine


@pytest.mark.unit_test
def test_combine_with_none_arg_returns_base() -> None:
    assert combine("base", None) == "base"


@pytest.mark.unit_test
def test_combine_with_singleton_arg_returns_base_slash_arg() -> None:
    assert combine("base", "a") == "base/a"


@pytest.mark.unit_test
def test_combine_with_multiple_args_returns_base_slash_joined() -> None:
    assert combine("base", "a", "b", "c") == "base/a/b/c"


@pytest.mark.unit_test
def test_base_values_are_unique() -> None:
    values = [member.value for member in Base]
    assert len(values) == len(set(values))
