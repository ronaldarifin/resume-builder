# Docker image name
IMAGE_NAME := resume-generator

# Build the Docker image
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
run:
	docker run --rm -v $(PWD)/output:/app/output $(IMAGE_NAME)

# Build and run
all: build run

.PHONY: build run all
