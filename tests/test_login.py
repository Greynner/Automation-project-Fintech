from playwright.sync_api import Page, expect
from pages.login_page import LoginPage
from config import VALID_USER, VALID_PASSWORD


def test_login_success(login_page: LoginPage, page: Page):
    """
    Escenario: Login exitoso.
    GIVEN que el usuario está en la pantalla de login
    WHEN ingresa credenciales válidas
    THEN debería ver un texto que solo aparece después de loguearse.
    """
    # WHEN
    login_page.login(VALID_USER, VALID_PASSWORD)

    # THEN: validamos que el usuario llegó a la página de productos
    expect(page.get_by_text("Products")).to_be_visible()
  


def test_login_fail(login_page: LoginPage):
    """
    Login fallido para que veas cómo manejar errores.
    """
    login_page.login("wrong_user", "wrong_pass")
    login_page.assert_login_error()