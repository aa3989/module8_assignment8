
"""Unit tests for calculator API logging."""

import logging
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_addition_logging(caplog):
    """Verify successful addition is logged."""
    with caplog.at_level(logging.INFO):
        response = client.post(
            "/add",
            json={"a": 10, "b": 5}
        )

    assert response.status_code == 200
    assert response.json()["result"] == 15
    assert "Add Operation Successful" in caplog.text


def test_division_logging(caplog):
    """Verify successful division is logged."""
    with caplog.at_level(logging.INFO):
        response = client.post(
            "/divide",
            json={"a": 10, "b": 2}
        )

    assert response.status_code == 200
    assert response.json()["result"] == 5
    assert "Divide Operation Successful" in caplog.text


def test_division_by_zero_logging(caplog):
    """Verify division by zero generates a warning."""
    with caplog.at_level(logging.WARNING):
        response = client.post(
            "/divide",
            json={"a": 10, "b": 0}
        )

    assert response.status_code == 400
    assert any(
        record.levelno == logging.WARNING
        and "Divide Operation Error" in record.message
        for record in caplog.records
    )
