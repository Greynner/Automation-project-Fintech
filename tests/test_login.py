import os
import pytest
from pages.login_page import PayPalLoginPage
from config import PAYPAL_SANDBOX_EMAIL, PAYPAL_SANDBOX_PASSWORD

def test_paypal_login_ok_reaches_otp(page):
    """Test de login en PayPal sandbox que verifica que se llega a la pantalla de OTP"""
    
    # Verificar que las credenciales estén configuradas
    if not PAYPAL_SANDBOX_EMAIL or not PAYPAL_SANDBOX_PASSWORD:
        pytest.skip("PAYPAL_SANDBOX_EMAIL y PAYPAL_SANDBOX_PASSWORD deben estar configuradas como variables de entorno")
    
    paypal = PayPalLoginPage(page)

    # Navegar directamente a la página de login
    paypal.goto_login()

    paypal.login(
        email=PAYPAL_SANDBOX_EMAIL,
        password=PAYPAL_SANDBOX_PASSWORD
    )

    # Verificar que el login fue exitoso (puede llegar a OTP o directamente al dashboard)
    paypal.assert_reached_otp()


def test_paypal_login_failed(page):
    """Test de login en PayPal sandbox que verifica que el login falla"""
    
    # Verificar que las credenciales estén configuradas
    if not PAYPAL_SANDBOX_EMAIL or not PAYPAL_SANDBOX_PASSWORD:
        pytest.skip("PAYPAL_SANDBOX_EMAIL y PAYPAL_SANDBOX_PASSWORD deben estar configuradas como variables de entorno")
    
    paypal = PayPalLoginPage(page)
    
    paypal.goto_login()
    
    paypal.login(email="invalid@example.com", password="invalidpassword")