import pytest
from playwright.sync_api import Page
from config import BASE_URL, VALID_USER, VALID_PASSWORD
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    """
    Deja la página en la pantalla de login y devuelve el Page Object listo.
    """
    lp = LoginPage(page)
    lp.goto(BASE_URL)
    return lp


@pytest.fixture
def dashboard_page(page: Page) -> DashboardPage:
    """
    Deja la página en el dashboard después de hacer login y devuelve el Page Object listo.
    """
@pytest.fixture
def dashboard_page(login_page):
    login_page.login(VALID_USER, VALID_PASSWORD)
    return DashboardPage(login_page.page)