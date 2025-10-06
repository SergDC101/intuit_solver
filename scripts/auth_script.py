import os

from loguru import logger

from data.env_var import INTUIT_LOGIN, INTUIT_PASSWORD
from page.auth_page import AuthPage


class AuthScript:

    def __init__(self, driver):
        self.driver = driver
        self.auth = AuthPage(self.driver)

    def login(self):
        self.auth.set_login(INTUIT_LOGIN)
        self.auth.set_password(INTUIT_PASSWORD)
        self.auth.click_sign_in()
        logger.info(f"Авторизация прошла успешно")