#################################################################################
# GLOBALS                                                                       #
#################################################################################

-include .envrc
export

PYTHON_INTERPRETER = python3

#################################################################################
# COMMANDS                                                                      #
#################################################################################

.PHONY: help pre-commit install clean test start

# Default target executed when no arguments are given to make.
all: help

help: ## Show this help screen.
	@grep -h -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'

pre-commit: ## Runs the pre-commit over entire repo
	@poetry run pre-commit run --all-files

define install_dependencies
	if ! type "poetry" > /dev/null; then \
		pip install poetry; \
	fi
	poetry config virtualenvs.in-project true
	poetry install --sync --with dev
endef

install: ## Install dependencies with Poetry.
	@$(call install_dependencies)

clean: ## Delete all Python cache files.
	@find . -type d -name "__pycache__" -prune -exec rm -rf {} \; &&\
	find . -type d -name ".pytest_cache" -prune -exec rm -rf {} \; &&\

test: ## Run all unit tests locally.
	@poetry run python -m pytest -s .

start: ## Run the project locally
	@poetry run zero_step_ml
