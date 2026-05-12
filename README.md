# fred-stl

A Python library for the [FRED API](https://fred.stlouisfed.org/docs/api/fred/) (Federal Reserve Economic Data, St. Louis Fed).

## Installation

```bash
pip install fred-stl
```

## Requirements

- Python 3.13+
- A [FRED API key](https://fred.stlouisfed.org/docs/api/api_key.html) (free, requires registration)

## Quick start

```python
import json
import urllib.parse
import urllib.request

from fred import category, for_request

params = category.RequestParams(
    api_key="your-api-key",
    file_type=category.FileType.json,
    category_id=0,
)

url = f"{category.ENDPOINT}?{urllib.parse.urlencode(for_request(params))}"

with urllib.request.urlopen(url) as resp:
    data = json.loads(resp.read())

response = category.Response.model_validate(data)
print(response.categories[0].name)  # "Categories"
```

## Usage

Each FRED endpoint is exposed as a module at the top level of the `fred` package. Every module provides:

- `RequestParams` — a typed, validated model for building requests
- `Response` — a typed, validated model for parsing responses
- `ENDPOINT` — the API endpoint URL
- Any enum types needed to construct a request (e.g. `FileType`, `SortOrder`)

Use `for_request` to convert a `RequestParams` instance into a `dict[str, str]` ready for any HTTP client:

```python
from fred import for_request, releases

params = releases.RequestParams(
    api_key="your-api-key",
    file_type=releases.FileType.json,
)

query = for_request(params)  # {"api_key": "...", "file_type": "json", ...}
```

## Available endpoints

### Category

| Module | Endpoint |
|--------|----------|
| `category` | `fred/category` |
| `category_children` | `fred/category/children` |
| `category_related` | `fred/category/related` |
| `category_series` | `fred/category/series` |
| `category_tags` | `fred/category/tags` |
| `category_related_tags` | `fred/category/related_tags` |

### Releases

| Module | Endpoint |
|--------|----------|
| `releases` | `fred/releases` |
| `releases_dates` | `fred/releases/dates` |
| `release` | `fred/release` |
| `release_dates` | `fred/release/dates` |
| `release_series` | `fred/release/series` |
| `release_sources` | `fred/release/sources` |
| `release_tags` | `fred/release/tags` |
| `release_related_tags` | `fred/release/related_tags` |
| `release_tables` | `fred/release/tables` |

### Series

| Module | Endpoint |
|--------|----------|
| `series` | `fred/series` |
| `series_categories` | `fred/series/categories` |
| `series_observations` | `fred/series/observations` |
| `series_release` | `fred/series/release` |
| `series_search` | `fred/series/search` |
| `series_search_tags` | `fred/series/search/tags` |
| `series_search_related_tags` | `fred/series/search/related_tags` |
| `series_tags` | `fred/series/tags` |
| `series_updates` | `fred/series/updates` |
| `series_vintagedates` | `fred/series/vintagedates` |

### Sources

| Module | Endpoint |
|--------|----------|
| `sources` | `fred/sources` |
| `source` | `fred/source` |
| `source_releases` | `fred/source/releases` |

### Tags

| Module | Endpoint |
|--------|----------|
| `tags` | `fred/tags` |
| `tags_related` | `fred/related_tags` |
| `tags_series` | `fred/tags/series` |


### Maps (GeoFRED)

| Module | Endpoint |
|--------|----------|
| `geofred_shapes` | `geofred/shapes/file` |
| `geofred_series_group` | `geofred/series/group` |
| `geofred_series_data` | `geofred/series/data` |
| `geofred_regional_data` | `geofred/regional/data` |

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).
