.PHONY: install
install:
	uv sync

.PHONY: migrate
migrate:
	uv run python manage.py migrate

.PHONY: makemigrations
makemigrations:
	uv run python manage.py makemigrations

.PHONY: runserver
runserver:
	uv run python manage.py runserver 0.0.0.0:8000

.PHONY: createsuperuser
createsuperuser:
	uv run python manage.py createsuperuser

.PHONY: collectstatic
collectstatic:
	uv run python manage.py collectstatic --noinput

.PHONY: shell
shell:
	uv run python manage.py shell