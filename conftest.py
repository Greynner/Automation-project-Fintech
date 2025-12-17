import pytest
from playwright.sync_api import Page
from config import PAYPAL_BASE_URL
from pages.login_page import PayPalLoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(page: Page) -> PayPalLoginPage:
    """
    Deja la página en la pantalla de login de PayPal y devuelve el Page Object listo.
    """
    lp = PayPalLoginPage(page)
    lp.goto()
    return lp


@pytest.fixture
def dashboard_page(login_page: PayPalLoginPage) -> DashboardPage:
    """
    Deja la página en el dashboard después de hacer login y devuelve el Page Object listo.
    """
    from config import PAYPAL_SANDBOX_EMAIL, PAYPAL_SANDBOX_PASSWORD
    login_page.goto_login()
    login_page.login(PAYPAL_SANDBOX_EMAIL, PAYPAL_SANDBOX_PASSWORD)
    return DashboardPage(login_page.page)