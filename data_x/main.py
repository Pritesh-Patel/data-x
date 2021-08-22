from .config.datax import DataXSchema
from .data import data
from .model import model
from .pipeline import pipeline


from pathlib import Path
import typer
import time
import sys
import os

from yaml import load, dump
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

from dask.distributed import Client

## add params
## Client(processes=False)

app = typer.Typer()
config_app = typer.Typer()
data_app = typer.Typer()
model_app = typer.Typer()
pipeline_app = typer.Typer()

app.add_typer(config_app, name='config')
app.add_typer(data_app, name='data')
app.add_typer(model_app, name='model')
app.add_typer(pipeline_app, name='pipeline')

datax_schema = DataXSchema()

def load_config(file):
    f = open(file)
    obj = load(f, Loader= Loader)
    datax_obj = datax_schema.load(obj)
    f.close()
    return datax_obj

###### CONFIG COMMANDS #####
@config_app.command()
def print_config(config_path: Path):
    config  = load_config(config_path)
    print('Config: {}'.format(dump(config)))

#### DATA COMMANDS ######
@data_app.command()
def info(config_path: Path, data_source: str):
    config  = load_config(config_path)
    data.info(config, data_source)

@data_app.command()
def describe(config_path: Path, data_source: str):
    config  = load_config(config_path)
    data.describe(config, data_source)

@data_app.command()
def profile(config_path: Path, data_source_name: str, minimal: bool = True):
    config  = load_config(config_path)
    data.profile(config, data_source_name, minimal)

#### MODEL COMMANDS ######
@model_app.command()
def print_model(config_path: Path, model_name: str):
    config  = load_config(config_path)
    m = model.get_model_config(config, model_name)
    print('Model Config: {}'.format(dump(m)))

#### PIPELINE COMMANDS ####
@pipeline_app.command()
def print_pipeline(config_path: Path, pipeline_name: str, detailed: bool = False):
    config  = load_config(config_path)

    if detailed == False:
        p = pipeline.get_pipeline_config(config, pipeline_name)
        print('Pipeline Config: {}'.format(dump(p)))
    else:
        ap = pipeline.get_assembled_pipeline_config(config, pipeline_name)
        print('Pipeline Config: {}'.format(dump(ap)))

@pipeline_app.command()
def run_pipeline(config_path: Path, pipeline_name: str):
    config  = load_config(config_path)
    ap = pipeline.get_assembled_pipeline_config(config, pipeline_name)
    print('Running Pipeline: {}'.format(dump(ap)))
    pipeline.run_assembled_pipeline(ap)

if __name__ == "__main__":
    app()
