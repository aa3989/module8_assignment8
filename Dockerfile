
FROM python:3.14-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# Install system dependencies and create non-root user
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libssl-dev && \
    rm -rf /var/lib/apt/lists/* && \
    groupadd -r appgroup && \
    useradd -r -g appgroup appuser

# Install Python dependencies
COPY requirements.txt .

RUN python -m pip install --no-cache-dir --upgrade \
        pip \
        "setuptools>=78.1.1" \
        wheel && \
    python -m pip install --no-cache-dir -r requirements.txt && \
    python -m pip install --no-cache-dir --upgrade \
        "msgpack>=1.2.1" \
        "setuptools>=78.1.1" \
        "urllib3>=2.8.0" && \
    python -m pip check

# Copy application
COPY --chown=appuser:appgroup . .

# Run as non-root user
USER appuser

EXPOSE 8000

# Health check using Python instead of curl
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=5)" || exit 1

# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "4"]
