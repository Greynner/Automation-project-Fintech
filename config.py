# config.py
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

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
# Keep these values in .env locally or GitHub Actions secrets in CI.
PAYPAL_SANDBOX_EMAIL = os.getenv("PAYPAL_SANDBOX_EMAIL")
PAYPAL_SANDBOX_PASSWORD = os.getenv("PAYPAL_SANDBOX_PASSWORD")
