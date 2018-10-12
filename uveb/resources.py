from flask_restful import Resource
from . import controllers

class CVideoResource(Resource):
    """Represents a CVideo Resource"""

    def get(self, id):
        return controllers.CVideoFetcher.fetch_by_id(id).serialize()
