ARG BASE_IMG=python:3.11-slim
FROM ${BASE_IMG}

# psutil requirements
RUN apt update && apt install -y gcc g++ libc-dev && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# install poetry and skip using virtualenvs
COPY pyproject.toml poetry.lock /app/
RUN pip install poetry && poetry config virtualenvs.create false
RUN poetry install

# Create a non-root user to run the app
RUN useradd -m appuser
USER appuser

COPY monitor /app/monitor

CMD [ "python", "monitor/main.py" ]