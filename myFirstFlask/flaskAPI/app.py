from flask import Flask, request

app = Flask(__name__)


stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "price": 17.99
            }
        ]
    }
]


@app.route("/store")
def get_stores():
    return {"stores": stores}


@app.route("/store", methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items": []}
    stores.append(new_store)
    # Always better to return JSON format data(dict in python)
    return new_store, 201


@app.route("/<string:store_name>/item", methods=['POST'])
def create_item(store_name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == store_name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": f"Store <{store_name}> not found!"}, 404


@app.route("/<string:store_name>/items", methods=['GET'])
def get_items(store_name):
    for store in stores:
        if store["name"] == store_name:
            return {"item": store["items"], "return_code": 201}, 201
    return {"message": f"Store <{store_name}> not found!"}, 404


if "__name__" == "__main__":
    app.run(debug=True)
