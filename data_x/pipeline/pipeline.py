from ..config.datax import DataX
from ..config.pipeline import Pipeline
from ..model import model
from ..model.model import Model
from ..data import data
from ..data.data import DataSource


class AssembledPipeline:
    def __init__(self, pipeline_name: str, artifacts_path: str, model: Model, train_ds: DataSource, test_ds: DataSource, labels_ds: DataSource):
        self.pipeline_name = pipeline_name
        self.artifacts_path = artifacts_path
        self.model = model
        self.train_ds = train_ds
        self.test_ds = test_ds
        self.labels_ds = labels_ds


def get_pipeline_config(config: DataX, pipeline: str) -> Pipeline:
    for p in config.pipeline:
        if p.name == pipeline:
            return p

    print("failed to find pipeline")


def get_assembled_pipeline_config(config: DataX, pipeline: str) -> AssembledPipeline:
    p = get_pipeline_config(config, pipeline)

    name = p.name
    artifacts_path = p.artifacts_path
    model_imp = model.get_model_config(config, p.train.model)
    train_ds = data.get_data_source_config(config, p.train.train_data_source)
    test_ds = data.get_data_source_config(config, p.train.test_data_source)
    labels_ds = data.get_data_source_config(config, p.train.labels_data_source)

    return AssembledPipeline(
        name,
        artifacts_path,
        model_imp,
        train_ds,
        test_ds,
        labels_ds
    )


def run_assembled_pipeline(ap: AssembledPipeline):
    train_df = data.load_data_source(ap.train_ds)
    test_df = data.load_data_source(ap.test_ds)
    labels = data.load_data_source(ap.labels_ds).columns.values.tolist()
    model_impl = ap.model
    model.train(model_impl, ap.artifacts_path, len(labels), train_df, test_df)
