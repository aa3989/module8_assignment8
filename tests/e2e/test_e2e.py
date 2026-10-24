# tests/e2e/test_e2e.py

import pytest  # Import the pytest framework for writing and running tests
from playwright.sync_api import expect
# The following decorators and functions define E2E tests for the FastAPI calculator application.

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    """Verify that the redesigned calculator homepage loads."""
    page.goto("http://localhost:8000")

    expect(page.locator("#calculator-heading")).to_have_text(
        "Calculator",
        timeout=10000
    )

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    """
    Test the addition functionality of the calculator.

    This test simulates a user performing an addition operation using the calculator
    on the frontend. It fills in two numbers, clicks the "Add" button, and verifies
    that the result displayed is correct.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '5'.
    page.fill('#b', '5')
    
    # Click the button that has the exact text "Add". This triggers the addition operation.
    page.click('button:text("Add")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly "Result: 15".
    # This verifies that the addition operation was performed correctly and the result is displayed as expected.
    expect(page.locator("#result")).to_have_text("15",timeout=10000)


@pytest.mark.e2e
def test_calculator_subtract(page, fastapi_server):
    """
    Test the subtraction functionality of the calculator.

    This test simulates a user subtracting two numbers
    through the web interface and verifies the result.
    """
    # Navigate to the homepage.
    page.goto("http://localhost:8000")

    # Enter the numbers.
    page.fill("#a", "10")
    page.fill("#b", "5")

    # Click the Subtract button.
    page.click('button:text("Subtract")')

    # Verify the subtraction result.
    expect(page.locator("#result")).to_have_text("5",timeout=10000)


@pytest.mark.e2e
def test_calculator_multiply(page, fastapi_server):
    """
    Test the multiplication functionality of the calculator.

    This test simulates a user multiplying two numbers
    through the web interface and verifies the result.
    """
    # Navigate to the homepage.
    page.goto("http://localhost:8000")

    # Enter the numbers.
    page.fill("#a", "10")
    page.fill("#b", "5")

    # Click the Multiply button.
    page.click('button:text("Multiply")')

    # Verify the multiplication result.
    expect(page.locator("#result")).to_have_text("50",timeout=10000)


@pytest.mark.e2e
def test_calculator_divide(page, fastapi_server):
    """
    Test the division functionality of the calculator.

    This test simulates a user dividing two numbers
    through the web interface and verifies the result.
    """
    # Navigate to the homepage.
    page.goto("http://localhost:8000")

    # Enter the numbers.
    page.fill("#a", "10")
    page.fill("#b", "2")

    # Click the Divide button.
    page.click('button:text("Divide")')

    # Verify the division result.
    expect(page.locator("#result")).to_have_text("5",timeout=10000)


@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    """
    Test the divide by zero functionality of the calculator.

    This test simulates a user attempting to divide a number by zero using the calculator.
    It fills in the numbers, clicks the "Divide" button, and verifies that the appropriate
    error message is displayed. This ensures that the application correctly handles invalid
    operations and provides meaningful feedback to the user.
    """
    # Navigate the browser to the homepage URL of the FastAPI application.
    page.goto('http://localhost:8000')
    
    # Fill in the first number input field (with id 'a') with the value '10'.
    page.fill('#a', '10')
    
    # Fill in the second number input field (with id 'b') with the value '0', attempting to divide by zero.
    page.fill('#b', '0')
    
    # Click the button that has the exact text "Divide". This triggers the division operation.
    page.click('button:text("Divide")')
    
    # Use an assertion to check that the text within the result div (with id 'result') is exactly
    # "Error: Cannot divide by zero!". This verifies that the application handles division by zero
    # gracefully and displays the correct error message to the user.
    expect(page.locator("#result")).to_have_text("Error: Cannot divide by zero!", timeout=10000)
