from ..config.datax import DataX
from ..config.model import Model

from . import nlp_st

import pandas as pd


def get_model_config(config: DataX, model: str) -> Model:
    for m in config.models:
        if m.name == model:
            return m

    print("failed to find model")


def not_found():
    print('model type not found')


def train(m: Model, out_path_prefix: str, num_of_labels: int, train_df: pd.DataFrame, test_df: pd.DataFrame):
    print('Training model type: {}'.format(m.type))

    model_builders = {
        'nlp-st': lambda: nlp_st.train(m, out_path_prefix, num_of_labels, train_df, test_df)
    }

    f = model_builders.get(m.type, not_found)
    f()
