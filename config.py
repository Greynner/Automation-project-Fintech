# config.py
import os

# config.py

# Base URL
PAYPAL_BASE_URL = "https://www.sandbox.paypal.com"
PAYPAL_LOGIN_URL = "https://www.sandbox.paypal.com/signin"

# Login flow
PAYPAL_LOGIN_LINK_TEXT = "Log In"

PAYPAL_EMAIL_SELECTOR = "#email"
PAYPAL_NEXT_SELECTOR = "#btnNext"

PAYPAL_PASSWORD_SELECTOR = "#password"
PAYPAL_SUBMIT_SELECTOR = "#btnLogin"

# OTP (assertion only)
PAYPAL_OTP_TITLE_TEXT = "Confirm your email"

# PayPal Sandbox Credentials
PAYPAL_SANDBOX_EMAIL = os.getenv("PAYPAL_SANDBOX_EMAIL", "sb-automationtest@business.example.com")
PAYPAL_SANDBOX_PASSWORD = os.getenv("PAYPAL_SANDBOX_PASSWORD", "4J^&shyx")

# Legacy credentials (para compatibilidad con test_dashboard.py)
# Nota: Estas variables se mantienen para compatibilidad, pero actualmente se usa PayPal sandbox
VALID_USER = os.getenv("VALID_USER", "standard_user")
VALID_PASSWORD = os.getenv("VALID_PASSWORD", "secret_sauce")
BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")