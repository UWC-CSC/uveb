import mysql.connector
from passlib.apps import custom_app_context as pwd_context
from contextlib import closing
from . import models

conn = None


def init(connection):
    global conn
    conn = connection


class ModelNotFoundException(Exception):
    pass


class UserFetcher(object):
    """Static class for operations with users"""

    global conn

    @staticmethod
    def fetch_by_username(username):
        """Fetches a models.User from the database using the username

        Arguments:
            username - The username of the user

        Returns:
            User - The requested User

        Raises:
            ModelNotFoundException - if the requested model is not found
        """
        with closing(conn.cursor()) as cur:
            cur.execute("""SELECT id, username, password_hash \
                    from users WHERE username=%s LIMIT 0, 1""", (username,))

            r = cur.fetchone()
            if r:
                return models.User(r[0], r[1], r[2][1:-1])
            else:
                raise ModelNotFoundException


class CVideoFetcher(object):
    """Static class for interfacing with the database"""

    _TABLE = 'c_videos'

    global conn

    @staticmethod
    def serialize_all(c_videos):
        """Utility method for serializing multiple CVideos

        Arguments:
            list - List of CVideos

        Returns:
            list - List of dictionaries representing serialized CVideos
        """
        serialized = []
        if c_videos:
            for cv in c_videos:
                serialized.append(cv.serialize())
            return serialized
        else:
            return None

    @staticmethod
    def fetch_all():
        """Fetches all partial models.CVideo's (only id and title) from the
           database.

        Returns:
            A list of all partial models.CVideo's
        """
        with closing(conn.cursor()) as cur:
            cur.execute("""SELECT id, title FROM """ + CVideoFetcher._TABLE)
            rows = cur.fetchall()

        cvideos = []
        for r in rows:
            cvideos.append(models.CVideo(r[0], r[1]))

        return cvideos

    @staticmethod
    def fetch_by_id(id):
        """Fetches a complete models.CVideo from the database

        Arguments:
            id - The id of the model.CVideo

        Returns:
            CVideo - the requested CVideo

        Raises:
            ModelNotFoundException - if the requested model is not found

        """
        with closing(conn.cursor()) as cur:
            cur.execute("""SELECT id, title, description, resolution_w, \
                        resolution_h, size, uri, path
                        FROM """ + CVideoFetcher._TABLE +
                        """ WHERE id=%s LIMIT 0, 1""", (id,))
            rows = cur.fetchone()

        if rows:
            r = rows
            return models.CVideo.full(r[0], r[1], r[2], (r[3], r[4]), r[5],
                                      r[6], r[7])
        else:
            raise ModelNotFoundException

    @staticmethod
    def push(cv):
        """Adds a new CVideo to the database

        Arguments:
            cv - The CVideo to insert
        """
        with closing(conn.cursor()) as cur:
            cur.execute("""INSERT INTO """ + CVideoFetcher._TABLE +
                        """(id, title, description, resolution_w, \
                        resolution_h, size, uri, path) VALUES \
                        (NULL, %s, %s, %s, %s, %s, %s, %s)""",
                        (cv.title, cv.description, cv.resolution[0],
                            cv.resolution[1], cv.size, cv.uri, cv.path))
            conn.commit()
