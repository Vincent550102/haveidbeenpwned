FROM python:3.10
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/etc/poetry python3 -
WORKDIR /app

COPY pyproject.toml poetry.lock .
RUN /etc/poetry/bin/poetry config virtualenvs.create false && \
    /etc/poetry/bin/poetry install
COPY . .
# ENTRYPOINT ["python", "/app/main.py"]
CMD ["sleep", "1000000"]
