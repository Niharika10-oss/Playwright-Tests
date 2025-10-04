# Playwright End-to-End Testing Project (Python/Pytest)

## 🌟 Project Overview

This repository showcases an automated end-to-end (E2E) testing suite built with **Playwright** and the **Pytest** testing framework in Python. The tests are designed to verify key user flows on the https://rahulshettyacademy.com/client

**Key Skills Demonstrated:**
* Test Automation using Python.
* Setup and execution of E2E tests across different browsers.


---

## 🛠️ Technology Stack

* **Language:** Python 3.x
* **Automation Framework:** Playwright for Python
* **Test Engine:** Pytest
* **Environment Manager:** Virtual Environments (`venv`)

---

## 🚀 Getting Started

Follow these steps to clone the repository and run the tests locally.

### 1. Prerequisites

Ensure you have [**Python 3.8+**] installed on your machine.

### 2. Setup

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/Niharika10-oss/Playwright-Tests.git](https://github.com/Niharika10-oss/Playwright-Tests.git)
    cd Playwright-Tests
    ```

2.  **Create and Activate a Virtual Environment (Recommended):**
    ```bash
    # Create the virtual environment
    python -m venv venv

    # Activate the virtual environment
    # On Windows:
    venv\Scripts\activate
    # On macOS/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    playwright install
    ```

### 3. Running the Tests

To execute the full test suite using Pytest, run the following command in your activated environment:

```bash
# Run all tests in headless mode (default)
pytest

# To run tests with a visible browser (headed mode):
pytest --headed
