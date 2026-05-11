.PHONY: up down dev dev-detach dev-down logs build clean

up:
	docker compose up --build -d

down:
	docker compose down

dev:
	docker compose -f docker-compose.dev.yml up --force-recreate --build

dev-detach:
	docker compose -f docker-compose.dev.yml up -d --force-recreate --build

dev-down:
	docker compose -f docker-compose.dev.yml down

logs:
	docker compose -f docker-compose.dev.yml logs -f

build:
	docker compose build
