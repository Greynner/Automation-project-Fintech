# Automation Project - Fintech Playwright

Test automation practice project using Playwright with Python.

## Description

This repository is designed as a practice project for people who want to move from Manual QA to QA Automation.

It uses a real-world testing structure with Python, Playwright, pytest, Page Objects, fixtures, environment-based configuration, GitHub Actions CI, and UI assertions. The goal is to help QA learners practice writing, organizing, and running automated browser tests.

The current sample flow is based on PayPal Sandbox login and send-money scenarios.

## Requirements

- Python 3.8+
- Playwright
- A PayPal Sandbox account if you want to run the end-to-end tests with real sandbox credentials

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Install Playwright browsers:
```bash
playwright install
```

## Environment Variables

Create a `.env` file from `.env.example`:

```bash
cp .env.example .env
```

Then fill in your own PayPal Sandbox values:

```env
PAYPAL_SANDBOX_EMAIL=
PAYPAL_SANDBOX_PASSWORD=
PAYPAL_RECIPIENT_EMAIL=
```

Do not commit real credentials to the repository.

## Usage

Run the tests:

```bash
pytest
```

Run with Playwright options:

```bash
pytest --browser=chromium --tracing on --video=retain-on-failure
```

If sandbox credentials are not configured, credential-dependent tests are skipped.

## Continuous Integration

GitHub Actions runs the Playwright test suite on pushes and Pull Requests to `main`.

CI uses these repository secrets when available:

- `PAYPAL_SANDBOX_EMAIL`
- `PAYPAL_SANDBOX_PASSWORD`
- `PAYPAL_RECIPIENT_EMAIL`

## Project Structure

- `config.py` - Configuration loaded from environment variables.
- `conftest.py` - Shared pytest fixtures.
- `pages/` - Page Objects for PayPal login and send-money flows.
- `tests/` - Automated tests.
- `.github/workflows/` - GitHub Actions CI workflows.
- `.github/CODEOWNERS` - Required code owner review rules.

## Contribution Policy

This repository is public, but changes to `main` should go through Pull Requests.

Repository protection is configured in GitHub so that:

- CI must pass before merging.
- Pull Requests require repository owner review.
- `.github/CODEOWNERS` marks `@Greynner` as the required reviewer for all files.
- Force pushes and branch deletion are disabled for `main`.
