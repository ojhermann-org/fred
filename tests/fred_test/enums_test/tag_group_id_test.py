import pytest

from fred.enums.tag_group_id import TagGroupID


@pytest.mark.contract_test
def test_freq_value() -> None:
    assert TagGroupID.freq == "freq"


@pytest.mark.contract_test
def test_gen_value() -> None:
    assert TagGroupID.gen == "gen"


@pytest.mark.contract_test
def test_geo_value() -> None:
    assert TagGroupID.geo == "geo"


@pytest.mark.contract_test
def test_geot_value() -> None:
    assert TagGroupID.geot == "geot"


@pytest.mark.contract_test
def test_rls_value() -> None:
    assert TagGroupID.rls == "rls"


@pytest.mark.contract_test
def test_seas_value() -> None:
    assert TagGroupID.seas == "seas"


@pytest.mark.contract_test
def test_src_value() -> None:
    assert TagGroupID.src == "src"


@pytest.mark.contract_test
def test_cc_value() -> None:
    assert TagGroupID.cc == "cc"
