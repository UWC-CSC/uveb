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
pip install -r requirements.txt
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

Deploying is done as per the [Flask Deployment
Guide](http://flask.pocoo.org/docs/1.0/tutorial/deploy/). 

Deploying is done using the `Makefile`. To package `Uveb`, run
```
make package
```
*two* times.

This produces a `.tar.gz` file which is hosted under releases on GitHub.

These are the releases that are hosted on GitHub releases.

To install the given release, download it and extract it:
```
tar -xzf uveb-*.tar.gz
cd uveb-*/
```

Install `Uveb` by running (*NOT* sudo):
```
make install
```

Now you can run `Uveb` by executing:
```
make run
```

This creates a localhost webserver at `127.0.0.1:8832`.

To deploy this, please connect it to `nginx` with a configuration similar to
this one:

```
server {
    listen 80;

    server_name _;

    access_log  /var/log/nginx/access.log;
    error_log  /var/log/nginx/error.log;

    location / {
        proxy_pass         http://127.0.0.1:8832/;
        proxy_redirect     off;

        proxy_set_header   Host                 $host;
        proxy_set_header   X-Real-IP            $remote_addr;
        proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto    $scheme;
    }
}
```

### Serving

To finally serve everything, create a folder for the software:
```bash
mkdir uveb/
cd uveb/
```

Download the latest `.whl` to your server.

Create a new `virtualenv` by running:
```bash
virtualenv venv
. venv/bin/activate
```

Finally, run `pip install uveb-x.x.x-none-any.whl`, where _x.x.x_ is the
release version. 

Also, do not forget to `export FLASK_APP=uveb`.

`uveb` is now installed, but you need to setup a database with which it can
interface.

This is relatively simple, using the available `schema.sql` create a `MySQL`
database:

Lastly, but probably most importantly, you have to configure `uveb`:
```bash
sudo mkdir /etc/uveb
sudo touch /etc/uveb/uveb.conf
sudo nano /etc/uveb/uveb.conf
```

Your `uveb` should work now, but you haven't installed `mysql` on your server
just yet. We recommend you use `mariadb`, just because it's more sensible.

Go ahead and install yourself a `mysql` implementation, set it up, etc.

Then, create a user for `uveb`:
```bash

```

### Configuration

The configuration follows the _Microsoft INI_ format. Currently the only
section available is `[Database]`.

```conf
[Database]
username = yourusername
password = yourpassword
```


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
