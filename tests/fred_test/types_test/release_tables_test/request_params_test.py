from pydantic import ValidationError
import pytest

from fred.enums.file_type import FileType
from fred.types.release_tables.request_params import RequestParams

_VALID_API_KEY = "abcdefghijklmnopqrstuvwxyz012345"
_VALID_RELEASE_ID = 53


@pytest.mark.contract_test
def test_accepts_valid_params() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
    )
    assert p.api_key == _VALID_API_KEY
    assert p.file_type == FileType.json
    assert p.release_id == _VALID_RELEASE_ID


@pytest.mark.contract_test
def test_element_id_defaults_to_none() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.element_id is None


@pytest.mark.contract_test
def test_accepts_explicit_element_id() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        element_id=12886,
    )
    assert p.element_id == 12886


@pytest.mark.contract_test
def test_include_observation_values_defaults_to_false() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.include_observation_values is False


@pytest.mark.contract_test
def test_accepts_include_observation_values_true() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        include_observation_values=True,
    )
    assert p.include_observation_values is True


@pytest.mark.contract_test
def test_observation_date_defaults_to_9999() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY, file_type=FileType.json, release_id=_VALID_RELEASE_ID
    )
    assert p.observation_date == "9999-12-31"


@pytest.mark.contract_test
def test_accepts_explicit_observation_date() -> None:
    p = RequestParams(
        api_key=_VALID_API_KEY,
        file_type=FileType.json,
        release_id=_VALID_RELEASE_ID,
        observation_date="2020-01-01",
    )
    assert p.observation_date == "2020-01-01"


@pytest.mark.contract_test
def test_rejects_missing_api_key() -> None:
    with pytest.raises(ValidationError):
        RequestParams(file_type=FileType.json, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_file_type() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, release_id=_VALID_RELEASE_ID)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_missing_release_id() -> None:
    with pytest.raises(ValidationError):
        RequestParams(api_key=_VALID_API_KEY, file_type=FileType.json)  # type: ignore[call-arg]


@pytest.mark.contract_test
def test_rejects_element_id_below_1() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            element_id=0,
        )


@pytest.mark.contract_test
def test_rejects_invalid_observation_date() -> None:
    with pytest.raises(ValidationError):
        RequestParams(
            api_key=_VALID_API_KEY,
            file_type=FileType.json,
            release_id=_VALID_RELEASE_ID,
            observation_date="not-a-date",
        )
