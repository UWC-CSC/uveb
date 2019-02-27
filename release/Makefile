CONFIG_LOCATION="/etc/uveb/uveb.conf"

install:
	pip install *.whl
	mkdir -p /etc/uveb
	cp uveb.conf /etc/uveb

uninstall:
	pip uninstall uveb
	rm -r /etc/uveb