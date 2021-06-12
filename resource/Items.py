from flask_restful import Resource, reqparse
from models.Items import ItemModel


class Items(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("title",type=str, required=True, help="Fill the field")
    parser.add_argument("price",type=float, required=True, help="Fill the field")
    parser.add_argument("desc",type=str, required=True, help="Fill the field")
    parser.add_argument("type",type=str, required=True, help="Fill the field")
    # parser.add_argument("id",type=int, required=True, help="Fill the field")


    def get(self):
        items = ItemModel.get_all_items()
        if len(items) == 0:
            return {"message": "no items in storage"}

        return {"all_items": [ item.json() for item in items]}

    def post(self):
        request_data = Items.parser.parse_args()
        item = ItemModel(**request_data)
        print(item.json())
        try:
            item.save_to_db()
        except Exception as e:
            print(e)
        return request_data


class ItemsAll(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("cart", type=list)
