from flask_restful import Resource, abort, reqparse
from . import controllers, models
from .config import Config

class IndexResource(Resource):
    """Represents the index resource"""

    def get(self):
        return {
                "version": Config.get_version(),
                "static": Config.get_static_server()
        }

class CVideosResource(Resource):
    """Represents multiple CVideo resource"""

    def get(self):
        return controllers.CVideoFetcher.serialize_all(
                controllers.CVideoFetcher.fetch_all()
        )


class CVideoResource(Resource):
    """Represents a CVideo Resource"""

    def get(self, id):
        try:
            return controllers.CVideoFetcher.fetch_by_id(id).serialize()
        except controllers.ModelNotFoundException:
            abort(404, message="Model not found")


class ProtectedCVideosResource(Resource):
    """Representes a CVideo resource requiring authentication

    Generally used for adding a new CVideo instance to the server. This class
    should be inherited from so that the auth.login_required decorator can be
    used.
    """

    def __init__(self):
        super().__init__()
        self._parser = reqparse.RequestParser()
        self._parser.add_argument('title')
        self._parser.add_argument('description')
        self._parser.add_argument('resolution')
        self._parser.add_argument('size')
        self._parser.add_argument('uri')
        self._parser.add_argument('path')

    def post(self):
        args = self._parser.parse_args()
        try:
            controllers.CVideoFetcher.push(models.CVideo.full(
                -1, args['title'], args['description'],
                tuple(args['resolution'].split('x')), args['size'],
                args['uri'], args['path']))
        except AttributeError as ae:
            abort(400)
