.PHONY: build

package:
	make build
	$(eval name := $(shell ls dist/*.whl | xargs -n 1 basename))
	cp dist/$(name) release/
	cp schema.sql release/
	cp -r release/ $(name)/
	tar -zcf $(name).tar.gz $(name)/
	make clean

build:
	python setup.py bdist_wheel

clean:
	rm -rf build
	rm -rf uveb.egg-info
	rm -rf dist
	rm -f release/*.whl
	rm -rf *.whl/

clean-all:
	make clean
	rm -r *.tar.gz

docs:
	make -C docs/Makefile