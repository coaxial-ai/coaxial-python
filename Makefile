# Setting up for local development
.PHONY: setup
setup:
	pip install -r requirements.txt

# Clean the /dist directory for a new publish
.PHONY: package-clean
package-clean:
	@rm -rf dist/*

# Build a new package into the /dist directory
.PHONY: package-build
package-build:
	python setup.py sdist

# Install the package into local virtual env
.PHONY: package-install
package-install:
	python setup.py install

# Test new package before publish
.PHONY: package-check
package-check:
	twine check dist/*

# Publish the new /dist package to Pypi
.PHONY: package-publish
package-publish:
	twine upload dist/*