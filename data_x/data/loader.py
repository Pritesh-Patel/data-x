from ..config.datasource import DataSource

import pandas as pd


def load_data_source(ds: DataSource) -> pd.DataFrame:
    if ds.type == 'local-labels-txt': #TODO: is there a better way to distinct labels from training data sources?
        with open(ds.path, 'r') as f:
            content = f.readline()
            labels = content.split(',')
            return pd.DataFrame(labels, columns =['labels'])

    if ds.compression == None:
        return pd.read_csv(ds.path)
    else:
        return pd.read_csv(ds.path, compression=ds.compression)
