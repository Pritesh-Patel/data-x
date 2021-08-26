from ..config.datasource import DataSource

import pandas as pd
from ast import literal_eval

def load_data_source(ds: DataSource) -> pd.DataFrame:
    if ds.type == 'local-labels-txt': #TODO: is there a better way to distinct labels from training data sources?
        with open(ds.path, 'r') as f:
            content = f.readline()
            labels = content.split(',')
            return pd.DataFrame(labels, columns =['labels'])

    opts = {'compression': ds.compression, 'nrows': ds.sample_size}

    return pd.read_csv(ds.path, **opts)
