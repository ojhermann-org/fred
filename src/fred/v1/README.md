# v1

This directory contains code related to [FRED API Version 1](https://fred.stlouisfed.org/docs/api/fred/).

Top-level code are shared types (e.g. `ApiKey`), while directories are named for particular data sets (e.g. `sources`).

Documentation

- [source](https://fred.stlouisfed.org/docs/api/fred/source.html)
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
    sources_OrderBy["sources/OrderBy"]
    sources_Response["sources/Response"]
    sources_Parameters["sources/Parameters"]

    source_Response --> Realtime

    source_Parameters --> ApiKey
    source_Parameters --> FileType
    source_Parameters --> Realtime

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
