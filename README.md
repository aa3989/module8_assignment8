# FastAPI Calculator — IS601 Module 8

A web-based calculator built with **FastAPI** a, with unit, integration, and browser end-to-end tests, application logging, and a GitHub Actions CI/CD workflow.

**GitHub:** https://github.com/aa3989/module8_assignment8  
**Docker Hub:** https://hub.docker.com/repository/docker/aby3989/module8_assignment8/general

## Features

- Addition, subtraction, multiplication, and division
- FastAPI JSON endpoints and a browser-based calculator interface
- Validation and error responses, including division-by-zero handling
- Application logging for successful calculations and errors
- Pytest unit and integration testing, plus Playwright browser tests
- GitHub Actions pipeline for testing, container security scanning, and Docker Hub deployment

## Tech stack

- Python **3.14** (tested locally with Python **3.14.4**)
- FastAPI, Uvicorn, Pydantic, Jinja2
- Pytest, pytest-cov, Playwright
- Docker, Docker Compose, GitHub Actions, Trivy

## Project structure

```text
module8_is601/
├── .github/workflows/test.yml     # CI/CD pipeline
├── app/
│   └── operations/
│       └── __init__.py            # add, subtract, multiply, divide
├── templates/
│   └── index.html                # calculator interface
├── tests/
│   ├── unit/                     # arithmetic and logging tests
│   ├── integration/              # FastAPI endpoint tests
│   ├── e2e/                      # Playwright browser tests
│   └── conftest.py               # shared pytest fixtures
├── main.py                       # FastAPI app, endpoints and logging
├── requirements.txt
├── pytest.ini
├── Dockerfile
├── docker-compose.yml
└── README.md
```



## Local installation (Ubuntu/WSL)

Clone the repository and enter the project directory:

```bash
git clone https://github.com/aa3989/module8_assignment8.git
cd module8_assignment8
```

Create and activate a Python 3.14 environment (requires Python 3.14 to be installed):

```bash
python3.14 -m venv venv
source venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install Chromium and the Linux libraries required by Playwright:

```bash
python -m playwright install --with-deps chromium
```

Start the app:

```bash
python -m uvicorn main:app --reload
```

Open **http://127.0.0.1:8000** to use the calculator. Interactive API documentation is available at **http://127.0.0.1:8000/docs**.

## API endpoints

| Method | Path | Purpose |
| --- | --- | --- |
| `GET` | `/` | Display the calculator web interface |
| `POST` | `/add` | Add two numbers |
| `POST` | `/subtract` | Subtract the second number from the first |
| `POST` | `/multiply` | Multiply two numbers |
| `POST` | `/divide` | Divide the first number by the second |

Example request:

```bash
curl -X POST http://127.0.0.1:8000/add \
  -H 'Content-Type: application/json' \
  -d '{"a":10,"b":5}'
```

Expected response:

```json
{"result":15.0}
```

Invalid requests return error information. Division by zero produces an HTTP `400` response.

## Testing

Run the full suite:

```bash
python -m pytest -v
```

Or run test categories separately:

```bash
python -m pytest tests/unit/ -v
python -m pytest tests/integration/ -v
python -m pytest tests/e2e/ -v
```

The `pytest.ini` configuration enables coverage reports. To request an explicit report:

```bash
python -m pytest tests/ -v --cov=app --cov-report=term-missing --cov-report=html
```

View `htmlcov/index.html` for the detailed HTML coverage report.

### Latest local results

| Test type | Passing tests |
| --- | ---: |
| Calculator unit tests | 21 |
| Logging tests | 3 |
| Integration tests | 5 |
| Playwright E2E tests | 3 |
| **Total** | **32 / 32** |



## Application logging

`main.py` uses Python's built-in `logging` module to record arithmetic operations and errors. Successful calculations are logged at `INFO`; expected errors such as division by zero can be logged at `WARNING`, while unexpected failures can be logged with tracebacks using `logger.exception()`.

To view logs, run the application in a terminal and perform calculations in the browser or through the API. Logging is also tested using pytest's `caplog` fixture.

## Docker

The project includes `Dockerfile` and `docker-compose.yml` files.

Build and run locally:

```bash
docker build -t module8_assignment8:local .
docker run --rm -p 8000:8000 module8_assignment8:local
```

Or use Docker Compose:

```bash
docker compose up --build
```

Then open **http://127.0.0.1:8000**.

