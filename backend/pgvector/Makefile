# Makefile

PWD := $(shell pwd)

APP_NAME=pgvector
DB_NAME=matcher
DB_USER=postgres
DB_PASSWORD=postgres

.PHONY: help
help:
	@echo "make options:"
	@awk -F ': ' '/^[^\t][a-z]/ && !/^[A-Z]/ {sub(":.*", ""); print}' Makefile

.PHONY: clean
clean:
	@docker stop $(APP_NAME) || true
	@docker rm $(APP_NAME) || true

.PHONY: build
build:
	@docker build -t $(APP_NAME) -f Dockerfile .

.PHONY: start
start:
	@docker run -d --name $(APP_NAME) -e POSTGRES_DB=$(DB_NAME) -e POSTGRES_USER=$(DB_USER) -e POSTGRES_PASSWORD=$(DB_PASSWORD) -p 5432:5432 $(APP_NAME):latest

.PHONY: all
all: clean build start
	@echo "starting all"
