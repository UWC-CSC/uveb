from urllib.parse import urlparse


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


class CVideo(ApiObject):
    """A object which represents a full, 360 video"""

    def __init__(self, id, title, description, resolution, size, uri, path):
        self.id = id
        self.title = title
        self.description = description
        self.resolution = resolution
        self.size = size
        self.uri = uri
        self.path = path

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
