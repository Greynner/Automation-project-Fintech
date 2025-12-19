import os
import pytest
from pages.send_money_page import SendMoneyPage
from pages.login_page import PayPalLoginPage
from config import PAYPAL_SANDBOX_EMAIL, PAYPAL_SANDBOX_PASSWORD

def test_paypal_send_money_e2e(page):
    # Primero hacer login
    login_page = PayPalLoginPage(page)
    login_page.goto_login()
    login_page.login(
        email=PAYPAL_SANDBOX_EMAIL,
        password=PAYPAL_SANDBOX_PASSWORD
    )
    login_page.assert_login_successful()
    
    # Luego enviar dinero
    send = SendMoneyPage(page)
    recipient = os.getenv("PAYPAL_RECIPIENT_EMAIL")  # sb-xxx@personal.example.com
    if not recipient:
        pytest.skip("PAYPAL_RECIPIENT_EMAIL debe estar configurada como variable de entorno")
    send.send_money(recipient_email=recipient, amount="0.01", note="Automation test")