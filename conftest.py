import pytest
from playwright.sync_api import Page
from config import PAYPAL_BASE_URL
from pages.login_page import PayPalLoginPage
from pages.send_money_page import SendMoneyPage
from pages.currency_converter_page import CurrencyConverterPage


@pytest.fixture
def login_page(page: Page) -> PayPalLoginPage:
    """
    Deja la página en la pantalla de login de PayPal y devuelve el Page Object listo.
    """
    lp = PayPalLoginPage(page)
    lp.goto()
    return lp


@pytest.fixture
def send_money_page(page: Page) -> SendMoneyPage:
    """
    Deja la página en la pantalla de Send Money y devuelve el Page Object listo.
    """
    sm = SendMoneyPage(page)
    sm.goto()
    return sm


@pytest.fixture
def currency_converter_page(page: Page) -> CurrencyConverterPage:
    """
    Deja la página en la pantalla del conversor de moneda de Littio y devuelve el Page Object listo.
    """
    cc = CurrencyConverterPage(page)
    cc.goto()
    return cc