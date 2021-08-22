from ..config.datasource import DataSource

import pandas as pd

def load_data_source(ds: DataSource) -> pd.DataFrame:
   if ds.compression == None:
      return pd.read_csv(ds.path)
   else:
      return pd.read_csv(ds.path, compression=ds.compression)