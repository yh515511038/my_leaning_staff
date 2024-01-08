from marshmallow import Schema, fields

'''
    Clear Structure to Validate requested data
    @blp.arguments(StoreSchema): validate requested data
    @blp.response(StoreSchema): define the responses in Swagger UI(return code and description)
'''

class ItemSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Float(required=True)
    store_id = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    name = fields.Str()
    price = fields.Float()


class StoreSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)
