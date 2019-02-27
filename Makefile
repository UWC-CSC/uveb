package:
	make build
	$(eval name := $(shell ls dist/*.whl | xargs -n 1 basename))
	cp dist/$(name) release/
	cp schema.sql release/

build:
	python setup.py bdist_wheel