CONFIG_LOCATION="/etc/uveb/uveb.conf"

run:
	( \
		source venv/bin/activate; \
		uwsgi --http 127.0.0.1:5000 --module uveb:app; \
	)

install:
	( \
		virtualenv venv; \
		source venv/bin/activate; \
		pip install *.whl; \
		mkdir -p /etc/uveb; \
		sudo cp uveb.conf /etc/uveb; \
		printf "\e[48;5;052m%03d This script does not set up your database."; \
		printf "Please set up your database"; \
		printf "\e[0m"; \
	)

uninstall:
	pip uninstall uveb
	rm -r /etc/uveb