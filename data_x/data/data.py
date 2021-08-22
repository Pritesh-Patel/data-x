from ..config.datasource import DataSource
from ..config.datax import DataX
from .loader import load_data_source

import pandas as pd
from pandas_profiling import ProfileReport


def get_data_source_config(config: DataX, data_source: str) -> DataSource:
    for ds in config.data_sources:
        if ds.name == data_source:
            return ds

    print("failed to find datasource")

# TODO cache with file hash?


def load_data_source_from_config(config: DataX, data_source: str) -> pd.DataFrame:
    ds = get_data_source_config(config, data_source)
    return load_data_source(ds)


def info(config: DataX, data_source: str):
    df = load_data_source_from_config(config, data_source)
    print(df.info())


def describe(config: DataX, data_source: str):
    df = load_data_source_from_config(config, data_source)
    print(df.describe())


def profile(config: DataX, data_source: str, minimal: bool):
    df = load_data_source_from_config(config, data_source)
    title = '{}'.format(data_source)
    profile = ProfileReport(df, minimal=minimal)
    profile.to_file('{}.html'.format(title))
