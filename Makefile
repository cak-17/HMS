SHELL := /bin/bash

include .env

.PHONY: help
help: ## Show this help
	@egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Make a new virtual environment
	python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: install
install: venv ## Make venv and install requirements
	$(BIN)/pip install --upgrade pip && $(BIN)/pip install -r requirements.txt

migrate: ## Make and run migrations
	$(PYTHON) manage.py makemigrations
	$(PYTHON) manage.py migrate

db-up: ## Pull and start the Docker Postgres container in the background
	docker pull postgres
	docker-compose up -d

db-shell: ## Access the Postgres Docker database interactively with psql
	docker exec -it container_name psql -d $(DBNAME)

.PHONY: test
test: ## Run tests
	$(PYTHON) $(APP_DIR)/manage.py test application --verbosity=0 --parallel --failfast

.PHONY: run
run: ## Run the Django 
	$(PYTHON) $(APP_DIR)/manage.py runserver

.PHONY: setup-backend
setup-backend: ## Init Empty Django Project
	django-admin startproject backend && $(PYTHON) $(APP_DIR)/backend/manage.py createsuperuser

django_repo: install migrate run ## Install requirements, apply migrations, then start development server
start_django: install setup-backend