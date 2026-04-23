import pytest

from fred.enums.order_by import (
    CategorySeries,
    CategoryTags,
    ReleaseRelatedTags,
    Releases,
    ReleasesDates,
    ReleaseSeries,
    ReleaseTags,
    SeriesSearchRelatedTags,
    SeriesSearchTags,
    SeriesTags,
)


@pytest.mark.contract_test
def test_category_series_series_id_value() -> None:
    assert CategorySeries.series_id == "series_id"


@pytest.mark.contract_test
def test_category_series_title_value() -> None:
    assert CategorySeries.title == "title"


@pytest.mark.contract_test
def test_category_series_units_value() -> None:
    assert CategorySeries.units == "units"


@pytest.mark.contract_test
def test_category_series_frequency_value() -> None:
    assert CategorySeries.frequency == "frequency"


@pytest.mark.contract_test
def test_category_series_seasonal_adjustment_value() -> None:
    assert CategorySeries.seasonal_adjustment == "seasonal_adjustment"


@pytest.mark.contract_test
def test_category_series_realtime_start_value() -> None:
    assert CategorySeries.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_category_series_realtime_end_value() -> None:
    assert CategorySeries.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_category_series_last_updated_value() -> None:
    assert CategorySeries.last_updated == "last_updated"


@pytest.mark.contract_test
def test_category_series_observation_start_value() -> None:
    assert CategorySeries.observation_start == "observation_start"


@pytest.mark.contract_test
def test_category_series_observation_end_value() -> None:
    assert CategorySeries.observation_end == "observation_end"


@pytest.mark.contract_test
def test_category_series_popularity_value() -> None:
    assert CategorySeries.popularity == "popularity"


@pytest.mark.contract_test
def test_category_series_group_popularity_value() -> None:
    assert CategorySeries.group_popularity == "group_popularity"


@pytest.mark.contract_test
def test_category_tags_series_count_value() -> None:
    assert CategoryTags.series_count == "series_count"


@pytest.mark.contract_test
def test_category_tags_popularity_value() -> None:
    assert CategoryTags.popularity == "popularity"


@pytest.mark.contract_test
def test_category_tags_created_value() -> None:
    assert CategoryTags.created == "created"


@pytest.mark.contract_test
def test_category_tags_name_value() -> None:
    assert CategoryTags.name == "name"


@pytest.mark.contract_test
def test_category_tags_group_id_value() -> None:
    assert CategoryTags.group_id == "group_id"


@pytest.mark.contract_test
def test_releases_release_id_value() -> None:
    assert Releases.release_id == "release_id"


@pytest.mark.contract_test
def test_releases_name_value() -> None:
    assert Releases.name == "name"


@pytest.mark.contract_test
def test_releases_press_release_value() -> None:
    assert Releases.press_release == "press_release"


@pytest.mark.contract_test
def test_releases_realtime_start_value() -> None:
    assert Releases.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_releases_realtime_end_value() -> None:
    assert Releases.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_releases_dates_release_date_value() -> None:
    assert ReleasesDates.release_date == "release_date"


@pytest.mark.contract_test
def test_releases_dates_release_id_value() -> None:
    assert ReleasesDates.release_id == "release_id"


@pytest.mark.contract_test
def test_releases_dates_release_name_value() -> None:
    assert ReleasesDates.release_name == "release_name"


@pytest.mark.contract_test
def test_release_series_series_id_value() -> None:
    assert ReleaseSeries.series_id == "series_id"


@pytest.mark.contract_test
def test_release_series_title_value() -> None:
    assert ReleaseSeries.title == "title"


@pytest.mark.contract_test
def test_release_series_units_value() -> None:
    assert ReleaseSeries.units == "units"


@pytest.mark.contract_test
def test_release_series_frequency_value() -> None:
    assert ReleaseSeries.frequency == "frequency"


@pytest.mark.contract_test
def test_release_series_seasonal_adjustment_value() -> None:
    assert ReleaseSeries.seasonal_adjustment == "seasonal_adjustment"


@pytest.mark.contract_test
def test_release_series_realtime_start_value() -> None:
    assert ReleaseSeries.realtime_start == "realtime_start"


@pytest.mark.contract_test
def test_release_series_realtime_end_value() -> None:
    assert ReleaseSeries.realtime_end == "realtime_end"


@pytest.mark.contract_test
def test_release_series_last_updated_value() -> None:
    assert ReleaseSeries.last_updated == "last_updated"


@pytest.mark.contract_test
def test_release_series_observation_start_value() -> None:
    assert ReleaseSeries.observation_start == "observation_start"


@pytest.mark.contract_test
def test_release_series_observation_end_value() -> None:
    assert ReleaseSeries.observation_end == "observation_end"


@pytest.mark.contract_test
def test_release_series_popularity_value() -> None:
    assert ReleaseSeries.popularity == "popularity"


@pytest.mark.contract_test
def test_release_series_group_popularity_value() -> None:
    assert ReleaseSeries.group_popularity == "group_popularity"


@pytest.mark.contract_test
def test_release_tags_series_count_value() -> None:
    assert ReleaseTags.series_count == "series_count"


@pytest.mark.contract_test
def test_release_tags_popularity_value() -> None:
    assert ReleaseTags.popularity == "popularity"


@pytest.mark.contract_test
def test_release_tags_created_value() -> None:
    assert ReleaseTags.created == "created"


@pytest.mark.contract_test
def test_release_tags_name_value() -> None:
    assert ReleaseTags.name == "name"


@pytest.mark.contract_test
def test_release_tags_group_id_value() -> None:
    assert ReleaseTags.group_id == "group_id"


@pytest.mark.contract_test
def test_release_related_tags_series_count_value() -> None:
    assert ReleaseRelatedTags.series_count == "series_count"


@pytest.mark.contract_test
def test_release_related_tags_popularity_value() -> None:
    assert ReleaseRelatedTags.popularity == "popularity"


@pytest.mark.contract_test
def test_release_related_tags_created_value() -> None:
    assert ReleaseRelatedTags.created == "created"


@pytest.mark.contract_test
def test_release_related_tags_name_value() -> None:
    assert ReleaseRelatedTags.name == "name"


@pytest.mark.contract_test
def test_release_related_tags_group_id_value() -> None:
    assert ReleaseRelatedTags.group_id == "group_id"


@pytest.mark.contract_test
def test_series_search_tags_series_count_value() -> None:
    assert SeriesSearchTags.series_count == "series_count"


@pytest.mark.contract_test
def test_series_search_tags_popularity_value() -> None:
    assert SeriesSearchTags.popularity == "popularity"


@pytest.mark.contract_test
def test_series_search_tags_created_value() -> None:
    assert SeriesSearchTags.created == "created"


@pytest.mark.contract_test
def test_series_search_tags_name_value() -> None:
    assert SeriesSearchTags.name == "name"


@pytest.mark.contract_test
def test_series_search_tags_group_id_value() -> None:
    assert SeriesSearchTags.group_id == "group_id"


@pytest.mark.contract_test
def test_series_search_related_tags_series_count_value() -> None:
    assert SeriesSearchRelatedTags.series_count == "series_count"


@pytest.mark.contract_test
def test_series_search_related_tags_popularity_value() -> None:
    assert SeriesSearchRelatedTags.popularity == "popularity"


@pytest.mark.contract_test
def test_series_search_related_tags_created_value() -> None:
    assert SeriesSearchRelatedTags.created == "created"


@pytest.mark.contract_test
def test_series_search_related_tags_name_value() -> None:
    assert SeriesSearchRelatedTags.name == "name"


@pytest.mark.contract_test
def test_series_search_related_tags_group_id_value() -> None:
    assert SeriesSearchRelatedTags.group_id == "group_id"


@pytest.mark.contract_test
def test_series_tags_series_count_value() -> None:
    assert SeriesTags.series_count == "series_count"


@pytest.mark.contract_test
def test_series_tags_popularity_value() -> None:
    assert SeriesTags.popularity == "popularity"


@pytest.mark.contract_test
def test_series_tags_created_value() -> None:
    assert SeriesTags.created == "created"


@pytest.mark.contract_test
def test_series_tags_name_value() -> None:
    assert SeriesTags.name == "name"


@pytest.mark.contract_test
def test_series_tags_group_id_value() -> None:
    assert SeriesTags.group_id == "group_id"
