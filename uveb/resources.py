from flask_restful import Resource, abort
from . import controllers


class CVideoResource(Resource):
    """Represents a CVideo Resource"""

    def get(self, id):
        try:
            return controllers.CVideoFetcher.fetch_by_id(id).serialize()
        except controllers.ModelNotFoundException:
            abort(404, message="Model not found")
