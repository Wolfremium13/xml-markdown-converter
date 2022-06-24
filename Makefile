.DEFAULT_GOAL := help

.PHONY: help
help:  ## Show this help
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: setup
setup: ## Setup local environment
	@pipenv install --dev

.PHONY: lint
lint:   ## Lint the project files
	@echo "Formatting with autopep8"
	@PIPENV_VERBOSITY=-1 pipenv run autopep8 -i -r ./
	@echo "Check for errors with flake8"
	@PIPENV_VERBOSITY=-1 pipenv run flake8 ./

.PHONY: tests
tests:  ## Locally run tests
	@PIPENV_VERBOSITY=-1 pipenv run pytest -v tests/

.PHONY: run-local
run-local: ## Runs locally the project
	@PIPENV_VERBOSITY=-1 pipenv run python -m src

OUTPUT_XML_FILE = ./data/updated-xml-data.xml
.PHONY: update-xml
update-xml: ## Updates the xml file
	@echo "Starting download of the xml file"
	@wget "https://podcast.carlosble.com/feed/podcast" --output-document=$(OUTPUT_XML_FILE)
	@echo "Finished download in $(OUTPUT_XML_FILE)"

.PHONY: build-image
build-image:  ## Create a docker image
	@docker build -t "xml-markdown-converter" $(PWD)

.PHONY: run-image
run-image:  ## Run docker image (needs build first)
	
	@docker run --rm --volume "$(PWD)/data":/data xml-markdown-converter make run-local