from playwright.sync_api import Page, expect

# 🔧 AJUSTA ESTOS TEXTOS A LA APP REAL
USERNAME_PLACEHOLDER = "Username"   # Ej: "Correo electrónico", "Usuario", "RUT o correo"
PASSWORD_PLACEHOLDER = "Password"          # Ej: "Contraseña", "Clave de acceso"
LOGIN_BUTTON_TEXT   = "Login"       # Ej: "Iniciar sesión", "Entrar", "Acceder"
ERROR_LOGIN_TEXT    = "Epic sadface: Username and password do not match any user in this service"  # Mensaje de error cuando el login falla


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

    # Locators
    @property
    def username_input(self):
        return self.page.get_by_placeholder(USERNAME_PLACEHOLDER)

    @property
    def password_input(self):
        return self.page.get_by_placeholder(PASSWORD_PLACEHOLDER)

    @property
    def login_button(self):
        return self.page.get_by_role("button", name=LOGIN_BUTTON_TEXT)

    @property
    def error_message(self):
        return self.page.get_by_text(ERROR_LOGIN_TEXT)

    # Actions
    def goto(self, base_url: str):
        # login está en /login, déjalo así.
        # Si está en la raíz, cambia a: self.page.goto(base_url)
        self.page.goto(base_url)

    def login(self, username: str, password: str):
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()

    # Assertions
    def assert_login_error(self):
        expect(self.error_message).to_be_visible()
