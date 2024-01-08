import uuid
from flask import Flask, request
from flask_smorest import Api, abort
from db import stores, items

from resources.store import blp as StoreBlueprint
from resources.item import blp as ItemBlueprint


app = Flask(__name__)

app.config["PROPAGATE_EXCEPTIONS"] = True
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"


# Register flask_smorest api with app
api = Api(app)
# Register blueprint with api
api.register_blueprint(StoreBlueprint)
api.register_blueprint(ItemBlueprint)

# @app.route("/store")
# def get_stores():
#     return {"stores": stores}


# @app.route("/store", methods=['POST'])
# def create_store():
#     store_data = request.get_json()
#     store_id = uuid.uuid4().hex
#     print(store_id)
#     new_store = {**store_data, "id": store_id}
#     stores[store_id] = new_store
#     # Always better to return JSON format data(dict in python)
#     return new_store, 201


# @app.route("/item", methods=['POST'])
# def create_item():
#     item_data = request.get_json()
#     if (
#         "name" not in item_data
#         or "price" not in item_data
#         or "store_id" not in item_data
#         ):
#         abort(
#             400,
#             message="Bad request! Ensure 'price', 'store_id' and 'name' are included  in the JSON payload."
#             )
#     store_id = item_data["store_id"]
#     name = item_data["name"]
    
#     # If item already exists
#     for item in items.values():
#         if (
#             item["name"] == name
#             and item["store_id"] == store_id
#         ):
#             abort(400, message="Item already exist!")
    
#     # If store not exists
#     if store_id not in stores:
#         abort(404, message=f"Store <{store_id}> not found!")
    
#     item_id = uuid.uuid4().hex
#     new_item = {**item_data, "id": item_id}
#     items[item_id] = new_item
#     return new_item, 201


# @app.route("/item", methods=['GET'])
# def get_items():
#     return {"items": list(items.values())}


# @app.route("/store/<string:store_id>", methods=['GET'])
# def get_store(store_id):
#     try:
#         return stores[store_id]
#     except KeyError:
#         abort(404, message="Store not found!>")


# @app.route("/item/<string:item_id>", methods=['GET'])
# def get_item(item_id):
#     try:
#         return items[item_id]
#     except KeyError:
#         abort(404, message="Item not found!>")


# @app.route("/item/<string:item_id>", methods=['DELETE'])
# def delete_item(item_id):
#     try:
#         del items[item_id]
#         return {"message": "Item deleted."}
#     except KeyError:
#         abort(404, message="Item not found!")


# @app.route("/item/<string:item_id>", methods=['PUT'])
# def update_item(item_id):
#     request_data = request.get_json()
#     if (
#         "name" not in request_data
#         or "price" not in request_data
#         or "store_id" not in request_data
#     ):
#         abort(404, message="Bad request! please check.")
    
#     toUpdatedItem = items[item_id]
#     # Update item with same item_id(Union operator)
#     toUpdatedItem |= request_data
    
#     return {"message": "Item updated."}



if "__name__" == "__main__":
    app.run(debug=True)
