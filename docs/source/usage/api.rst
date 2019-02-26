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

