import mysql.connector
from contextlib import closing
from . import models

conn = None


def init(connection):
    global conn
    conn = connection


class ModelNotFoundException(Exception):
    pass


class CVideoFetcher(object):
    """Static class for interfacing with the database"""

    global conn

    @staticmethod
    def fetch_by_id(id):
        """Fetches a models.CVideo from the database

        Arguments:
            id - The id of the model.CVideo

        Returns:
            CVideo - the requested CVideo

        Throws:
            ModelNotFoundException - if the requested model is not found

        """
        with closing(conn.cursor()) as cur:
            cur.execute("""SELECT id, title, description, resolution_w, \
                    resolution_h, size, uri, path
                    FROM c_videos WHERE id=%s""", (id,))
            r = cur.fetchone()

            if r:
                return models.CVideo(r[0], r[1], r[2], (r[3], r[4]), r[5],
                                     r[6], r[7])
            else:
                raise ModelNotFoundException
