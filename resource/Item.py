from flask_restful import Resource, reqparse
from models.Items import ItemModel

class Item(Resource):

    def get(self, id):
        item = ItemModel.find_by_id(id)
        # print(item.json())
        if item:
            return {"item": item.json()}, 200

        return {"item": "no such item"}, 404
