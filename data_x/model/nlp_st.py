from ..config.model import Model

import torch
import pandas as pd
from simpletransformers.classification import MultiLabelClassificationModel
from ast import literal_eval


def multilabel(m: Model, out_path_prefix: str, num_of_labels: int, train_df: pd.DataFrame, test_df: pd.DataFrame,  cuda=torch.cuda.is_available()):
    #TODO remove once transformation code is implemented expensive
    train_df['labels'] = train_df['labels'].apply(literal_eval)
    test_df['labels'] = test_df['labels'].apply(literal_eval)
    
    MODEL = m.variant
    MODEL_CASE = f'{MODEL}-base-uncased'
    MODEL_ARTIFACT_OUT_PREFIX = f'{out_path_prefix}/{m.name}'
    MODEL_BEST_OUT = f'{MODEL_ARTIFACT_OUT_PREFIX}/best'
    MODEL_RESULT_OUT = f'{MODEL_ARTIFACT_OUT_PREFIX}/results'
    MODEL_TENSORBOARD_OUT = f'{MODEL_ARTIFACT_OUT_PREFIX}/tensorboard'

    train_args = m.params

    if train_args.get('output_dir') == None:
        train_args['output_dir'] = MODEL_RESULT_OUT

    if train_args.get('best_model_dir') == None:
        train_args['best_model_dir'] = MODEL_BEST_OUT

    if train_args.get('tensorboard_dir') == None:
        train_args['tensorboard_dir'] = MODEL_TENSORBOARD_OUT

    model = MultiLabelClassificationModel(
        MODEL,
        MODEL_CASE,
        num_labels=num_of_labels,
        args=train_args,
        use_cuda=cuda
    )

    model.train_model(train_df, eval_df=test_df)


def not_found():
    ## TODO: proper error, force quit pipeline
    print('task type not found')


def train(m: Model, out_path_prefix: str, num_of_labels: int, train_df: pd.DataFrame, test_df: pd.DataFrame):
    model_builders = {
        'multilabel': lambda: multilabel(m, out_path_prefix, num_of_labels, train_df, test_df)
    }
    f = model_builders.get(m.task, not_found)
    f()
