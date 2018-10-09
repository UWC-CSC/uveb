from flask_restful import Resource
from c_video import CVideo
from c_video_fetcher import CVideoFetcher

class CVideoResource(Resource):
    """Represents a CVideo Resource"""

    def get(self, id):
        return CVideoFetcher.fetch_by_id(id).serialize()
