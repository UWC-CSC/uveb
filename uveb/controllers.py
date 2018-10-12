import mysql.connector
from contextlib import closing
from . import models


class CVideoFetcher(object):
    """Static class for interfacing with the database"""
    _conn = None

    def init(connection):
        CVideoFetcher._conn = connection

    @staticmethod
    def fetch_by_id(id):
        with closing(CVideoFetcher._conn.cursor()) as cur:
            cur.execute("""SELECT id, title, description, resolution_w, \
                    resolution_h, size, uri, path
                    FROM c_videos WHERE id=%s""", (id,))

            r = cur.fetchone()

            return models.CVideo(r[0], r[1], r[2], (r[3], r[4]), r[5], r[6],
                                 r[7])
