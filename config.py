# config.py
import os

# URL del entorno (luego cambiar por la real)
BASE_URL = os.getenv("APP_BASE_URL", "https://www.saucedemo.com/")

# Usuario de pruebas
VALID_USER = os.getenv("APP_LOGIN_USER", "standard_user")
VALID_PASSWORD = os.getenv("APP_LOGIN_PASSWORD", "secret_sauce")