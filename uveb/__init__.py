from flask import Flask
from flask_restful import Resource, Api, abort
from . import resources, controllers, credentials
from flask_httpauth import HTTPBasicAuth
import mysql.connector

app = Flask(__name__)
api = Api(app)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    try:
        return (controllers.UserFetcher.fetch_by_username(username)
                                       .verify_password(password))
    except controllers.ModelNotFoundException:
        abort(401)


class ProtectedCVideosResource(resources.ProtectedCVideosResource):
    decorators = [auth.login_required]


api.add_resource(resources.CVideosResource, '/cvideos')
api.add_resource(ProtectedCVideosResource, '/cvideos')
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
