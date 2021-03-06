from .camelcase import CamelCaseSchema

from marshmallow import fields,  post_load


class DataSource:
    def __init__(self, name, type, path, compression=None, sample_size = None):
        self.name = name
        self.type = type
        self.path = path
        self.compression = compression
        self.sample_size = sample_size

    def __repr__(self):
        return "<DataSource(source={self.name!r})>".format(self=self)


class DataSourceSchema(CamelCaseSchema):
    # TODO validation

    name = fields.Str()
    type = fields.Str()
    path = fields.Str()
    compression = fields.Str()
    sample_size = fields.Float()

    @post_load
    def make_datasource(self, data, **kwargs):
        return DataSource(**data)
