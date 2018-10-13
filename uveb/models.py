from urllib.parse import urlparse
from passlib.apps import custom_app_context as pwd_context


class ApiObject(object):
    """An abstract class which provides functions for passing to Structure
    classes
    """

    def serialize(self):
        """Should return a python dictionary resembling the structure of a JSON
        serialized object

        Returns:
            dict - Serialized dictionary of values
        """
        raise NotImplementedError('Class %s does not implement serialize()' %
                                  (self.__class__.__name__))


class User(ApiObject):
    """An object representing a user"""

    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    @property
    def id(self):
        """The id of the User"""
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def username(self):
        """The username of the User"""
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password_hash(self):
        """The password_hash of the User"""
        return self._password_hash

    @password_hash.setter
    def password_hash(self, password_hash):
        self._password_hash = password_hash

    def hash_password(self, password):
        """Encrypts a password and stores its hash as an attribute"""
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        """Checks if the entered password is correct for the user"""
        print(self.username)
        print(self.password_hash)
        return pwd_context.verify(password, self.password_hash)


class CVideo(ApiObject):
    """A object which represents a full, 360 video"""

    def __init__(self, id, title):
        self.id = id
        self.title = title

    @classmethod
    def full(CVideo, id, title, description, resolution, size, uri, path):
        """Overloaded constructor"""
        cv = CVideo(id, title)
        cv.description = description
        cv.resolution = resolution
        cv.size = size
        cv.uri = uri
        cv.path = path
        return cv

    @property
    def id(self):
        """The id of the video"""
        return self._id

    @id.setter
    def id(self, id):
        self._id = id

    @property
    def title(self):
        """The title of the video"""
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    @property
    def description(self):
        """The description of the video"""
        return self._description

    @description.setter
    def description(self, description):
        self._description = description

    @property
    def uri(self):
        """A string with the HTTP URL"""
        return self._uri.geturl()

    @uri.setter
    def uri(self, uri):
        self._uri = urlparse(uri)

    @property
    def resolution(self):
        """A tuple containing the resolution of the video"""
        return (self._res_w, self._res_h)

    @resolution.setter
    def resolution(self, resolution):
        self._res_w = resolution[0]
        self._res_h = resolution[1]

    @property
    def path(self):
        """The local URI of the video"""
        return self._path

    @path.setter
    def path(self, path):
        self._path = path

    @property
    def size(self):
        """The size of the file"""
        return self._size

    @size.setter
    def size(self, size):
        self._size = size

    def serialize(self):
        try:
            return {
                    'id': self.id,
                    'title': self.title,
                    'description': self.description,
                    'resolution': {
                        'w': self.resolution[0],
                        'h': self.resolution[1]
                    },
                    'size': self.size,
                    'uri': self.uri
            }
        except AttributeError:
            return {
                    'id': self.id,
                    'title': self.title
            }
