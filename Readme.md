
# UI Automation Framework

## Project Overview

This project contains a UI Automation Framework built using Python, Selenium, and Pytest. It is designed to automate test cases for the [OpenCart Demo Site](https://naveenautomationlabs.com/opencart/index.php?route=common/home).

---

## Features

- **Cross-browser testing** with Selenium WebDriver.
- **Page Object Model (POM)** design pattern for scalable and maintainable test code.
- **Pytest** integration for running and managing test cases.
- Automatic **HTML reporting**.
- **Screenshots** captured for failed tests.
- Parallel test execution using **pytest-xdist**.

---

## Project Structure

```bash
root
│
├─── ui_automation
│    ├─── tests               # Test cases
│    ├─── pages               # Page Object Model classes
│    ├─── reports             # HTML test reports
│    └─── screenshots         # Captured screenshots
│
├─── venv                     # Python virtual environment
│
├─── requirements.txt          # Project dependencies
│
└─── pytest.ini                # Pytest configurations

