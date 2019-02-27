API
===

The JSON API of Uveb is relatively simple and should prove easy to use.

The following endpoints are available.

``/``
-----

Handles general information.

``GET``
~~~~~~~

Returns a JSON object containing the following information:

::

	{
		"version": "currentVersion",
		"static": "staticPath"
	}

where

* ``currentVersion`` is the used version of Uveb
* ``staticPath`` is the path to the statically hosted files

*Example*:

::

	curl uveb/

returns

::

	{
		"version": "DEV",
		"static": "/var/www/static"
	}

``/cvideos``
------------

Handles general data of all *cvideos* (videos handled by Uveb)

``GET``
~~~~~~~

Returns a JSON array containing the following information:

::

	[
		{
			"id": idOfVideo,
			"title": "titleOfVideo",
			"description": "descriptionOfVideo",
			"thumbnail": "pathToThumbnail"
		},

		{
			...
		},

		...

	]

where

* ``idOfVideo`` - the id of the video
* ``titleOfVideo`` - the video title
* ``descriptionOfVideo`` - the video description
* ``pathToThumbnail`` - the url to the thumbnail

*Example*:

::

	curl uveb/cvideos

returns

::

	[
		{
			"id": 1,
			"title": "Rollercoaster Endeavor",
			"description": "The rollercoaster adventures of Jim",
			"thumbnail": "http://freeThumbnailHosting.fake/jimmy.png"
		},

		{
			"id": 2,
			"title": "A Cat's Adventures",
			"description": "The adventures of Bob the cat",
			"thumbnail": "http://freeThumbnailHosting.fake/bobby.png"
		}

	]

``/cvideos/{id}``
-----------------

Handles the detailed information of a ``cvideo``.

Arguments:
* ``{id}`` - the id of the ``cvideo``

``GET``
~~~~~~~

Returns a JSON object containing the detailed information of the ``cvideo``.

::

	{
		"id": cvideoId,
		"title": "cvideoTitle",
		"description": "cvideoDescription",
		"resolution": {
			"w": cvideoWidth,
			"h": cvideoHeight
		},
		"size": cvideoSize,
		"uri": "cvideoUri"
	}

where

* ``cvideoId`` - the id of the video
* ``cvideoTitle`` - the title of the video
* ``cvideoDescription`` - the video description
* ``cvideoWidth`` - the width of the video
* ``cvideoHeight`` - the height of the video
* ``cvideoSize`` - the size of the video in bytes
* ``cvideoUri`` - the uri where the cvideo is accessible at

*Example*:

::

	{
		"id": 1,
		"title": "Rollercoaster Endeavor",
		"description": "The rollercoaster adventures of Jim",
		"resolution": {
			"w": 800,
			"h": 600
		},
		"size": 5652749,
		"uri": "http://freevideohosting.fake/jimmy.mp4"
	}