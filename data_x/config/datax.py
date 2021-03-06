
from marshmallow import fields, post_load
from .pipeline import PipelineSchema
from .model import ModelSchema
from .datasource import DataSourceSchema
from .camelcase import CamelCaseSchema


class DataX:
    def __init__(self, data_sources, models, pipelines):
        self.data_sources = data_sources
        self.models = models
        self.pipeline = pipelines


class DataXSchema(CamelCaseSchema):
    data_sources = fields.List(fields.Nested(DataSourceSchema))
    models = fields.List(fields.Nested(ModelSchema))
    pipelines = fields.List(fields.Nested(PipelineSchema))

    @post_load
    def make_datax(self, data, **kwargs):
        return DataX(**data)
