import pytest

from client.v1.sources.parameters import ParametersBuilder
from fred.v1.sources.parameters import Parameters

VALID_KEY = "a1b2c3d4e5f6a1b2c3d4e5f6a1b2c3d4"


@pytest.mark.smoke_test
def test_build_defaults_match_parameters_defaults() -> None:
    assert ParametersBuilder(api_key=VALID_KEY).build() == Parameters(api_key=VALID_KEY)
