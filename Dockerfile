FROM python:3.10-slim
ENV PYTHONUNBUFFERED True

RUN pip install --upgrade pip poetry && pip cache purge

COPY poetry.lock pyproject.toml ./
RUN poetry config virtualenvs.create false \
    && poetry install --no-cache

COPY . /
