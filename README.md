# Uveb

Uveb is the backend for UWCCSC VR Experience. It is RESTful API.

## Getting Started

These instructions will get you a copy of the project up and running on your
local machine for development and testing purposes. See deployment for notes on
how to deploy the project on a live system.

### Prerequisites

This project requires `python3.7`, `virtualenv`, `pip` and `mysql`.


### Installing

These instructions will set up a development version of `uveb` on your machine.

First clone the repository.

```
git clone https://github.com/UWC-CSC/uveb.git
```

After that, create and activate a virtualenv in the repository:

```
virtualenv venv
. venv/bin/activate
```

Install the dependencies:

```
pip install flask
pip install flask-restful
pip install pycodestyle
```

Start the `mysql` server:
```
systemctl start mysqld
```

Now, set the application exports:

```
export FLASK_APP=uveb
export FLASK_ENV=development
```

And start the `flask` server:
```
flask run
```

Now, you can navigate to `localhost:5000` and see if there is a response.

## Running the tests

You can run the unit tests:
```
python -m unittest tests/*.py
```

### Coding style

The coding style is `pep8`. You can run tests with

```
pycodestyle uveb/*.py tests/*.py
```

## Deployment

Development is unprepared.

## Built With

* [Python](https://www.python.org/)
* [Flask](http://flask.pocoo.org/)
* [Flask-RESTful](https://flask-restful.readthedocs.io/en/latest/)

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Marko Vejnovic** - *Initial work* - 

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the
[GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) license. Check the
[LICENSE](LICENSE.md) file for more information.

## Acknowledgments

* Just [PurpleBooth](https://gist.github.com/PurpleBooth/109311bb0361f32d87a2)
  for her more-than-excellent README template.
