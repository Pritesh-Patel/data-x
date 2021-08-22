from .camelcase import CamelCaseSchema
from marshmallow import fields,  post_load

class TrainStep:
    def __init__(self, model, train_data_source, test_data_source, labels_data_source):
        self.model = model
        self.train_data_source = train_data_source
        self.test_data_source = test_data_source
        self.labels_data_source = labels_data_source

    def __repr__(self):
        return "<TrainStep(name={self.model!r})>".format(self=self)

class TrainStepSchema(CamelCaseSchema):
    #TODO validation

    model = fields.Str()
    train_data_source = fields.Str()
    test_data_source = fields.Str()
    labels_data_source = fields.Str()
    
    @post_load
    def make_datasource(self, data, **kwargs):
        return TrainStep(**data)

class Pipeline:
    def __init__(self, name, artifacts_path, train):
        self.name = name
        self.artifacts_path = artifacts_path
        self.train = train

    def __repr__(self):
        return "<Pipeline(name={self.name!r})>".format(self=self)
    


class PipelineSchema(CamelCaseSchema):
    #TODO validation

    name = fields.Str()
    artifacts_path = fields.Str()
    train = fields.Nested(TrainStepSchema)

    @post_load
    def make_datasource(self, data, **kwargs):
        return Pipeline(**data)