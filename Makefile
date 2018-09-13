# Project variables
PROJECT_NAME ?= todobackend

# Filename
DEV_COMPOSE_FILE := docker/dev/docker-compose.yml
REL_COMPOSE_FILE := docker/release/docker-compose.yml

# Docker Compose Project Names
REL_PROJECT := $(PROJECT_NAME)$(BUILD_TAG)
DEV_PROJECT := $(REL_PROJECT)dev

.PHONY: test release clean

test:
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) up --build test

release:
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) run --rm app manage.py collectstatic --noinput
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) run --rm app manage.py migrate --noinput
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) up --build test

clean:
	docker-compose -p $(DEV_PROJECT) -f $(DEV_COMPOSE_FILE) down
	docker-compose -p $(REL_PROJECT) -f $(REL_COMPOSE_FILE) down