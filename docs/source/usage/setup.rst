.. highlight:: bash

Setup
=====

Setting up Uveb is done in 8 steps. Currently, Uveb is not ready for a stable release. Please keep in mind the security issues.

Requirements
------------

Uveb requires the following prerequisites:

+--------------------+----------------------------------+-------------------------------------+-------------------------------------------------------------------+
| Name *Untested*    | Ubuntu *Untested*                | Arch                                | CentOS *Untested*                                                 |
+====================+==================================+=====================================+===================================================================+
| :code:`python3`    | :code:`apt install python3`      | :code:`pacman -S python`            | :code:`yum install centos-release-scl && yum install rh-python36` |
+--------------------+----------------------------------+-------------------------------------+-------------------------------------------------------------------+
| :code:`pip`        | :code:`apt install python3-pip`  | :code:`pacman -S python-pip`        | :code:`yum install python36-setuptools && easy_install-3.6 pip`   |
+--------------------+----------------------------------+-------------------------------------+-------------------------------------------------------------------+
| :code:`virtualenv` | :code:`pip3 install virtualenv`  | :code:`pacman -S python-virtualenv` | :code:`pip3 install virtualenv`                                   |
+--------------------+----------------------------------+-------------------------------------+-------------------------------------------------------------------+
| :code:`mariadb`    | :code:`pacman -S mariadb-server` | :code:`pacman -S mariadb`           | :code:`yum install mariadb-server`                                |
+--------------------+----------------------------------+-------------------------------------+-------------------------------------------------------------------+

Clone
-----

Clone Uveb through :code:`git`

::

	git clone https://github.com/UWC-CSC/uveb.git && cd uveb

Virtualenv
----------

I recommend installing a :code:`virtualenv`, however if you do not wish to use 
:code:`virtualenv` you are free to skip this step altogether, however incorrect
setup may occur.

::

	virtualenv venv
	. venv/bin/activate

Dependencies
------------

Install the required modules. Please read what :code:`requirements.txt` entails
before you run the following command.

::

	pip install -r requirements.txt

MySQL
-----

Start the MySQL server:

::

	systemctl start mysqld

Optionally, you may choose to enable the MySQL server on startup:

::

	systemctl enable mysqld

Database Setup
--------------

The database you installed is empy and you must set it up before proceeding.

Login as the root user:

::

	mysql -u root -p

Create the :code:`uveb` database which will contain all of the data of the
application:

.. highlight:: sql

::

	CREATE DATABASE uveb;

Create the user which will use the database:

::

	GRANT ALL PRIVILEGES ON *.* TO 'uveb_username'@'localhost' IDENTIFIED BY 'secure_password';
	FLUSH PRIVILEGES;

Dump all of the tables from the provided :code:`schema.sql` (read it before you
execute the command!):

.. highlight:: bash

::

	mysql -u uveb_username --password=secure_password uveb < uveb/schema.sql

Uveb Config
-----------

Uveb itself is relatively easy to configure. Please check the :ref:`configuration
manual` for more information. Uveb *must* be manually configured.

Run
----

Now that everything is configured, you may run the application.

::

	export FLASK_APP=uveb
	export FLASK_ENV=development
	flask run --host=0.0.0.0
