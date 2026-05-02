import pytest

from fred.enums.shape import Shape


@pytest.mark.contract_test
def test_bea_value() -> None:
    assert Shape.bea == "bea"


@pytest.mark.contract_test
def test_msa_value() -> None:
    assert Shape.msa == "msa"


@pytest.mark.contract_test
def test_frb_value() -> None:
    assert Shape.frb == "frb"


@pytest.mark.contract_test
def test_necta_value() -> None:
    assert Shape.necta == "necta"


@pytest.mark.contract_test
def test_state_value() -> None:
    assert Shape.state == "state"


@pytest.mark.contract_test
def test_country_value() -> None:
    assert Shape.country == "country"


@pytest.mark.contract_test
def test_county_value() -> None:
    assert Shape.county == "county"


@pytest.mark.contract_test
def test_censusregion_value() -> None:
    assert Shape.censusregion == "censusregion"


@pytest.mark.contract_test
def test_censusdivision_value() -> None:
    assert Shape.censusdivision == "censusdivision"
