.. _uveb-conf:

Uveb Configuration
==================

Uveb's configuration is done through an ``.ini``-like file:

::

	/etc/uveb/uveb.conf

This configuration file *must* exist in order for Uveb to run.

This file is divided into sections as such:

::

	[section1]
	key1=value1
	key2=value2

	[section2]
	key3=value3

Sections
--------

The following sections and keys are available.

Database
~~~~~~~~

This section deals with options regarding database connection.

The available keys are:
* *username* - a string of the *database* username
* *password* - a string of the *database* password

Example
-------

The bare minimum Uveb configuration file is this one:

::

	[Database]
	username=myusername
	password=mypassword