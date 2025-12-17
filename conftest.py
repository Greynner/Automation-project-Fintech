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
def dashboard_page(page: Page) -> DashboardPage:
    """
    Deja la página en el dashboard después de hacer login y devuelve el Page Object listo.
    """
    pass