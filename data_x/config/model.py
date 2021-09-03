from .camelcase import CamelCaseSchema

from marshmallow import fields,  post_load


class Model:
    def __init__(self, name, type, variant, task, params):
        self.name = name
        self.type = type
        self.variant = variant
        self.task = task
        self.params = params

    def __repr__(self):
        return "<Model(name={self.name!r})>".format(self=self)

class ModelSchema(CamelCaseSchema):
    # TODO validation

    name = fields.Str()
    type = fields.Str()
    variant = fields.Str()
    task = fields.Str()
    params = fields.Dict()

    @post_load
    def make_datasource(self, data, **kwargs):
        return Model(**data)
