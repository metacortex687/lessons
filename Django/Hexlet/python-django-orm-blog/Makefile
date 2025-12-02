MANAGE := uv run python manage.py

.PHONY: test
test:
	uv run pytest

.PHONY: setup
setup: db-clean install migrate

.PHONY: install
install:
	@uv sync

.PHONY: db-clean
db-clean:
	@if exist db.sqlite3 del db.sqlite3

.PHONY: migrate
migrate:
	@$(MANAGE) migrate

.PHONY: shell
shell:
	@$(MANAGE) shell_plus --ipython

.PHONY: lint
lint:
	uv run ruff check python_django_orm_blog
