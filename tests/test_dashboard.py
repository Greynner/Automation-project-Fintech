from playwright.sync_api import Page, expect
from pages.dashboard_page import DashboardPage
from config import VALID_USER, VALID_PASSWORD


def test_add_to_cart(dashboard_page: DashboardPage, page: Page):
    """
    Escenario: Agregar un item al carrito.
    GIVEN que el usuario está en la pantalla de dashboard
    WHEN agrega un item al carrito
    THEN debería ver que el botón cambió a "Remove".
    """
    # WHEN
    dashboard_page.add_to_cart("Sauce Labs Backpack")

    # THEN: validamos que el item fue agregado al carrito (el botón debe decir "Remove")
    dashboard_page.assert_item_added_to_cart("Sauce Labs Backpack")

def test_remove_from_cart(dashboard_page: DashboardPage, page: Page):
    """
    Escenario: Remover un item del carrito.
    GIVEN que el usuario está en la pantalla de dashboard
    WHEN remueve un item del carrito
    THEN debería ver que el botón cambió a "Add to cart".
    """
    # GIVEN: primero agregamos el item al carrito
    dashboard_page.add_to_cart("Sauce Labs Backpack")
    
    # WHEN: removemos el item del carrito
    dashboard_page.remove_from_cart("Sauce Labs Backpack")

    # THEN: validamos que el item fue removido del carrito (el botón debe decir "Add to cart")
    dashboard_page.assert_item_not_added_to_cart("Sauce Labs Backpack")

def test_add_multiple_items_to_cart(dashboard_page: DashboardPage, page: Page):
    """
    Escenario: Agregar múltiples items al carrito.
    GIVEN que el usuario está en la pantalla de dashboard
    WHEN agrega múltiples items al carrito
    THEN debería ver que todos los botones cambiaron a "Remove".
    """
    # WHEN: agregamos múltiples items al carrito
    dashboard_page.add_to_cart("Sauce Labs Backpack")
    dashboard_page.add_to_cart("Sauce Labs Bike Light")
    dashboard_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    dashboard_page.add_to_cart("Sauce Labs Fleece Jacket")
    dashboard_page.add_to_cart("Sauce Labs Onesie")
    dashboard_page.add_to_cart("Test.allTheThings() T-Shirt (Red)")

    # THEN: validamos que todos los items fueron agregados al carrito
    dashboard_page.assert_item_added_to_cart("Sauce Labs Backpack")
    dashboard_page.assert_item_added_to_cart("Sauce Labs Bike Light")
    dashboard_page.assert_item_added_to_cart("Sauce Labs Bolt T-Shirt")
    dashboard_page.assert_item_added_to_cart("Sauce Labs Fleece Jacket")
    dashboard_page.assert_item_added_to_cart("Sauce Labs Onesie")
    dashboard_page.assert_item_added_to_cart("Test.allTheThings() T-Shirt (Red)")

def test_remove_multiple_items_from_cart(dashboard_page: DashboardPage, page: Page):
    """
    Escenario: Remover múltiples items del carrito.
    GIVEN que el usuario está en la pantalla de dashboard
    WHEN remueve múltiples items del carrito
    THEN debería ver que los botones cambiaron a "Add to cart".
    """
    # GIVEN: primero agregamos todos los items al carrito
    dashboard_page.add_to_cart("Sauce Labs Backpack")
    dashboard_page.add_to_cart("Sauce Labs Bike Light")
    dashboard_page.add_to_cart("Sauce Labs Bolt T-Shirt")
    dashboard_page.add_to_cart("Sauce Labs Fleece Jacket")
    dashboard_page.add_to_cart("Sauce Labs Onesie")
    dashboard_page.add_to_cart("Test.allTheThings() T-Shirt (Red)")
    
    # WHEN: removemos múltiples items del carrito
    dashboard_page.remove_from_cart("Sauce Labs Backpack")
    dashboard_page.remove_from_cart("Sauce Labs Bike Light")
    dashboard_page.remove_from_cart("Sauce Labs Bolt T-Shirt")
    dashboard_page.remove_from_cart("Sauce Labs Fleece Jacket")

    # THEN: validamos que los items fueron removidos del carrito
    dashboard_page.assert_item_not_added_to_cart("Sauce Labs Backpack")
    dashboard_page.assert_item_not_added_to_cart("Sauce Labs Bike Light")
    dashboard_page.assert_item_not_added_to_cart("Sauce Labs Bolt T-Shirt")
    dashboard_page.assert_item_not_added_to_cart("Sauce Labs Fleece Jacket")
    # Estos dos deberían seguir en el carrito
    dashboard_page.assert_item_added_to_cart("Sauce Labs Onesie")
    dashboard_page.assert_item_added_to_cart("Test.allTheThings() T-Shirt (Red)")
