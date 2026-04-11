import pytest

from fred.enums.filter_value import (
    SeriesUpdates,
    SourceReleases,
    Sources,
    Tags,
    TagsSeries,
)


@pytest.mark.contract_test
def test_series_updates_macro_value() -> None:
    assert SeriesUpdates.macro == "macro"


@pytest.mark.contract_test
def test_series_updates_regional_value() -> None:
    assert SeriesUpdates.regional == "regional"


@pytest.mark.contract_test
def test_series_updates_all_value() -> None:
    assert SeriesUpdates.all == "all"


@pytest.mark.contract_test
def test_sources_source_id_value() -> None:
    assert Sources.source_id == "source_id"


@pytest.mark.contract_test
def test_sources_name_value() -> None:
    assert Sources.name == "name"


@pytest.mark.contract_test
def test_sources_realtime_start_value() -> None:
    assert Sources.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_sources_realtime_end_value() -> None:
    assert Sources.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_source_releases_release_id_value() -> None:
    assert SourceReleases.release_id == "release_id"


@pytest.mark.contract_test
def test_source_releases_name_value() -> None:
    assert SourceReleases.name == "name"


@pytest.mark.contract_test
def test_source_releases_press_release_value() -> None:
    assert SourceReleases.press_release == "press_release"


@pytest.mark.contract_test
def test_source_releases_realtime_start_value() -> None:
    assert SourceReleases.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_source_releases_realtime_end_value() -> None:
    assert SourceReleases.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_tags_series_count_value() -> None:
    assert Tags.series_count == "series_count"


@pytest.mark.contract_test
def test_tags_popularity_value() -> None:
    assert Tags.popularity == "popularity"


@pytest.mark.contract_test
def test_tags_created_value() -> None:
    assert Tags.created == "created"


@pytest.mark.contract_test
def test_tags_name_value() -> None:
    assert Tags.name == "name"


@pytest.mark.contract_test
def test_tags_group_id_value() -> None:
    assert Tags.group_id == "group_id"


@pytest.mark.contract_test
def test_tags_series_series_id_value() -> None:
    assert TagsSeries.series_id == "series_id"


@pytest.mark.contract_test
def test_tags_series_title_value() -> None:
    assert TagsSeries.title == "title"


@pytest.mark.contract_test
def test_tags_series_units_value() -> None:
    assert TagsSeries.units == "units"


@pytest.mark.contract_test
def test_tags_series_frequency_value() -> None:
    assert TagsSeries.frequency == "frequency"


@pytest.mark.contract_test
def test_tags_series_seasonal_adjustment_value() -> None:
    assert TagsSeries.seasonal_adjustment == "seasonal_adjustment"


@pytest.mark.contract_test
def test_tags_series_realtime_start_value() -> None:
    assert TagsSeries.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_tags_series_realtime_end_value() -> None:
    assert TagsSeries.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_tags_series_last_updated_value() -> None:
    assert TagsSeries.last_updated == "last_updated"


@pytest.mark.contract_test
def test_tags_series_observation_start_value() -> None:
    assert TagsSeries.observation_start == "observation_start"


@pytest.mark.contract_test
def test_tags_series_observation_end_value() -> None:
    assert TagsSeries.observation_end == "observation_end"


@pytest.mark.contract_test
def test_tags_series_popularity_value() -> None:
    assert TagsSeries.popularity == "popularity"


@pytest.mark.contract_test
def test_tags_series_group_popularity_value() -> None:
    assert TagsSeries.group_popularity == "group_popularity"
