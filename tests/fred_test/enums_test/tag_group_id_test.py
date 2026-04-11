import pytest

from fred.enums.tag_group_id import TagGroupID


@pytest.mark.contract_test
def test_frequency_value() -> None:
    assert TagGroupID.frequency == "freq"


@pytest.mark.contract_test
def test_general_value() -> None:
    assert TagGroupID.general == "gen"


@pytest.mark.contract_test
def test_concept_value() -> None:
    assert TagGroupID.concept == "gen"


@pytest.mark.contract_test
def test_geography_value() -> None:
    assert TagGroupID.geography == "geo"


@pytest.mark.contract_test
def test_geotraphy_type_value() -> None:
    assert TagGroupID.geotraphy_type == "geot"


@pytest.mark.contract_test
def test_release_value() -> None:
    assert TagGroupID.release == "rls"


@pytest.mark.contract_test
def test_seasonal_adjustment_value() -> None:
    assert TagGroupID.seasonal_adjustment == "seas"


@pytest.mark.contract_test
def test_source_value() -> None:
    assert TagGroupID.source == "src"
