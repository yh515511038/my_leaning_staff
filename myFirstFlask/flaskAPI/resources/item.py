import uuid
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from db import items, stores
from schemas import ItemSchema, ItemUpdateSchema


blp = Blueprint("items", __name__, description="Operations on items")


@blp.route("/item")
class ItemList(MethodView):
    @blp.response(200, ItemSchema(many=True))
    def get(self):
        return items.values()

    # The JSON format `request_data` will be validated by `ItemSchema` first, then used here.
    @blp.arguments(ItemSchema)
    @blp.response(201, ItemSchema)
    def post(self, request_data):
        # request_data = request.get_json()
        for item in items.values():
            if (request_data["name"] == item["name"] and
                request_data['store_id'] == item['store_id']):
                abort(400, message="Item already exist!")
        
        if request_data["store_id"] not in stores:
            abort(404, message=f"Store <{request_data['store_id']}> not found!")
        
        item_id = uuid.uuid4().hex
        new_item = {**request_data, "id": item_id}
        items[item_id] = new_item
        return new_item, 201


@blp.route('/item/<string:item_id>')
class Item(MethodView):
    @blp.response(200, ItemSchema)
    def get(self, item_id):
        try:
            return items[item_id]
        except KeyError:
            abort(404, message='Item not found!')
    
    
    def delete(self, item_id):
        try:
            del items[item_id]
            return {"message": "Item deleted."}
        except KeyError:
            abort(404, message='Item not found!')

    # The request data should put as the first parameter
    @blp.arguments(ItemUpdateSchema)
    @blp.response(200, ItemSchema)
    def put(self, update_data, item_id):
        # update_data = request.get_json()
        try:
            items[item_id] |= update_data
            return items[item_id]
        except KeyError:
            abort(404, message='Item not found!')
