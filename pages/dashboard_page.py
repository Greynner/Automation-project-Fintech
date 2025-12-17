from playwright.sync_api import Page, expect

# 🔧 AJUSTA ESTOS TEXTOS A LA APP REAL
USERNAME_PLACEHOLDER = "Username"   # Ej: "Correo electrónico", "Usuario", "RUT o correo"
PASSWORD_PLACEHOLDER = "Password"          # Ej: "Contraseña", "Clave de acceso"
LOGIN_BUTTON_TEXT   = "Login"       # Ej: "Iniciar sesión", "Entrar", "Acceder"
ERROR_LOGIN_TEXT    = "Epic sadface: Username and password do not match any user in this service"  # Mensaje de error cuando el login falla


class DashboardPage:
    def __init__(self, page: Page):
        self.page = page

# Locators
    @property
    def page_title(self):
        return self.page.get_by_text("Products")

    @property
    def inventory_items(self):
        return self.page.locator(".inventory_item")
    @property
    def inventory_item_name(self):
        return self.page.locator(".inventory_item_name")
    @property
    def inventory_item_price(self):
        return self.page.locator(".inventory_item_price")
    @property
    def inventory_item_description(self):
        return self.page.locator(".inventory_item_description")
    @property
    def inventory_item_add_to_cart(self):
        return self.page.locator(".inventory_item_add_to_cart")

    # Actions
    def add_to_cart(self, item_name: str):
        """Agrega un item al carrito buscando por su nombre"""
        item_container = self.inventory_items.filter(has_text=item_name).first
        item_container.locator("button").first.click()

    def remove_from_cart(self, item_name: str):
        """Remueve un item del carrito buscando por su nombre"""
        item_container = self.inventory_items.filter(has_text=item_name).first
        item_container.locator("button").first.click()

    # Assertions
    def assert_item_added_to_cart(self, item_name: str):
        """Verifica que un item está en el carrito (el botón debe decir 'Remove')"""
        item_container = self.inventory_items.filter(has_text=item_name).first
        button = item_container.locator("button").first
        expect(button).to_have_text("Remove")

    def assert_item_not_added_to_cart(self, item_name: str):
        """Verifica que un item NO está en el carrito (el botón debe decir 'Add to cart')"""
        item_container = self.inventory_items.filter(has_text=item_name).first
        button = item_container.locator("button").first
        expect(button).to_have_text("Add to cart")
