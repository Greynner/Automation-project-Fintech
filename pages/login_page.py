from playwright.sync_api import Page, expect
from config import (
    PAYPAL_BASE_URL,
    PAYPAL_LOGIN_URL,
    PAYPAL_LOGIN_LINK_TEXT,
    PAYPAL_EMAIL_SELECTOR,
    PAYPAL_NEXT_SELECTOR,
    PAYPAL_PASSWORD_SELECTOR,
    PAYPAL_SUBMIT_SELECTOR,
    PAYPAL_OTP_TITLE_TEXT,
)

class PayPalLoginPage:
    def __init__(self, page: Page):
        self.page = page

    @property
    def login_link(self):
        return self.page.get_by_role("link", name=PAYPAL_LOGIN_LINK_TEXT)

    @property
    def email_input(self):
        return self.page.locator(PAYPAL_EMAIL_SELECTOR)

    @property
    def next_button(self):
        return self.page.locator(PAYPAL_NEXT_SELECTOR)

    @property
    def password_input(self):
        return self.page.locator(PAYPAL_PASSWORD_SELECTOR)

    @property
    def submit_button(self):
        return self.page.locator(PAYPAL_SUBMIT_SELECTOR)

    @property
    def otp_title(self):
        return self.page.get_by_text(PAYPAL_OTP_TITLE_TEXT)

    def goto(self):
        self.page.goto(PAYPAL_BASE_URL, wait_until="domcontentloaded")

    def goto_login(self):
        """Navega directamente a la página de login de PayPal"""
        self.page.goto(PAYPAL_LOGIN_URL, wait_until="domcontentloaded")

    def open_login(self):
        """Intenta abrir el login desde la página principal (puede fallar si el enlace no está visible)"""
        try:
            self.login_link.click(timeout=5000)
        except:
            # Si no encuentra el enlace, navega directamente a la página de login
            self.goto_login()

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.next_button.click()
        self.password_input.fill(password)
        self.submit_button.click()

    def assert_reached_otp(self):
        """Verifica que se llegó a la pantalla de OTP (si es requerida)"""
        # Esperar un poco para que la página cargue
        self.page.wait_for_timeout(2000)
        # Intentar verificar OTP, pero si no está, verificar que el login fue exitoso
        try:
            expect(self.otp_title).to_be_visible(timeout=3000)
        except:
            # Si no hay OTP, verificar que el login fue exitoso (redirige al dashboard)
            current_url = self.page.url
            assert "/mep/dashboard" in current_url or "/myaccount" in current_url or "/home" in current_url or "dashboard" in current_url, \
                f"Login no exitoso. URL actual: {current_url}"
    
    def assert_login_successful(self):
        """Verifica que el login fue exitoso verificando la URL del dashboard"""
        self.page.wait_for_timeout(2000)
        current_url = self.page.url
        assert "/mep/dashboard" in current_url or "/myaccount" in current_url or "/home" in current_url or "dashboard" in current_url, \
            f"Login no exitoso. URL actual: {current_url}"