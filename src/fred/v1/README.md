# v1

This directory contains code related to [FRED API Version 1](https://fred.stlouisfed.org/docs/api/fred/).

Top-level code are shared types (e.g. `ApiKey`), while directories are named for particular data sets (e.g. `sources`).

Documentation

- [source](https://fred.stlouisfed.org/docs/api/fred/source.html)
- [source_releases](https://fred.stlouisfed.org/docs/api/fred/source_releases.html)
- [sources](https://fred.stlouisfed.org/docs/api/fred/sources.html)

Dependencies

```mermaid
graph TD
    ApiKey
    FileType
    Realtime
    SortOrder

    source_Response["source/Response"]
    source_Parameters["source/Parameters"]
    source_releases_OrderBy["source_releases/OrderBy"]
    source_releases_Response["source_releases/Response"]
    source_releases_Parameters["source_releases/Parameters"]
    sources_OrderBy["sources/OrderBy"]
    sources_Response["sources/Response"]
    sources_Parameters["sources/Parameters"]

    source_Response --> Realtime

    source_Parameters --> ApiKey
    source_Parameters --> FileType
    source_Parameters --> Realtime

    source_releases_Response --> Realtime
    source_releases_Response --> SortOrder
    source_releases_Response --> source_releases_OrderBy

    source_releases_Parameters --> ApiKey
    source_releases_Parameters --> FileType
    source_releases_Parameters --> Realtime
    source_releases_Parameters --> SortOrder
    source_releases_Parameters --> source_releases_OrderBy

    sources_Response --> Realtime
    sources_Response --> sources_OrderBy
    sources_Response --> SortOrder
    sources_Response --> source_Response

    sources_Parameters --> ApiKey
    sources_Parameters --> FileType
    sources_Parameters --> Realtime
    sources_Parameters --> sources_OrderBy
    sources_Parameters --> SortOrder
```
