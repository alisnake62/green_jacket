FROM python:3.8

WORKDIR "/usr/src/app/"

COPY poetry.lock ./
COPY pyproject.toml ./
RUN pip install poetry
RUN poetry install