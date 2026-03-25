install:
	pip install -e .[dev]

run-api:
	uvicorn apps.api.main:app --reload

test:
	pytest

validate-data:
	python pipelines/data_validation.py

train:
	python apps/training/train.py

format:
	black .
	isort .

lint:
	ruff check .