FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY pyproject.toml pyproject.lock* requirements.txt* ./

RUN python -m pip install --upgrade pip

RUN bash -lc "\
    if [ -f requirements.txt ]; then \
        pip install --no-cache-dir -r requirements.txt; \
    elif [ -f pyproject.toml ]; then \
        pip install --no-cache-dir build && python -m pip install --no-cache-dir . ; \
    else \
        pip install --no-cache-dir streamlit polars sqlalchemy psycopg2-binary plotly python-dotenv pandas; \
    fi"

COPY . .

RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser

EXPOSE 8501

CMD ["streamlit", "run", "src/dashboard.py", "--server.port=8501", "--server.address=0.0.0.0", "--server.headless=true"]