from flask import Flask
from flask_restful import Resource, Api
from . import resources, controllers, credentials
import mysql.connector

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'World'}


api.add_resource(HelloWorld, '/')
api.add_resource(resources.CVideosResource, '/cvideos')
api.add_resource(resources.CVideoResource, '/cvideos/<string:id>')


@app.before_first_request
def initialize():
    connection = mysql.connector.connect(
            host='localhost',
            user=credentials.SQL_USERNAME,
            passwd=credentials.SQL_PASSWORD,
            database='uveb'
    )
    controllers.init(connection)


if __name__ == '__main__':
    app.run(debug=True)
