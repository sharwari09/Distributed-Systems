from flask import Flask
from flask_restful import Resource, Api, request
import sys

app = Flask(__name__)
api = Api(app)

entry_list = []
HTTP_PORT = int(sys.argv[1])


class Entries(Resource):
    def get(self):
        return {
                   "num_entries": len(entry_list),
                   "entries": entry_list
               }, 200

    def post(self):
        payload = request.get_json()
        entry_list.append(payload)
        return 201


api.add_resource(Entries,
                 '/api/v1/entries',
                 '/entries')


if __name__ == '__main__':
    app.run(port=HTTP_PORT, debug=True)