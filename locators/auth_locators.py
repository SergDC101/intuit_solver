from selenium.webdriver.common.by import By

class AuthLocators:
    LOGIN = (By.NAME, "name")
    PASSWORD = (By.NAME, "pass")
    BUTTON_SIGN_IN = (By.NAME, "op")

    