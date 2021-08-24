# Data X [WIP]

Data X aims to be a swiss army knife for producing production ready models.

It works with 3 main 'modules':

- DataSource (the sources of data to train models)
- Model (the type of model, tasks & params eg distillbert, multilabel)
- Pipeline (composed of datasources and a model)

You can see example configuration in the example directory.
## Pip install
To install via pip you can clone the directory and run `make -C data-x install` TODO: make installable via git + pip

## Poetry install
To install first install poetry, clone the repo and run `poetry install` TODO: pip package

Once installed you can use `data-x --help` to explore configured modules and do various tasks

To kick off the pipeline you can use `data-x pipeline run-pipeline ./config.yml  <PIPELINE_NAME>`

TODO: Better README & documentation