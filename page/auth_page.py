from base.selenium_base import SeleniumBase
from locators.auth_locators import AuthLocators


class AuthPage(SeleniumBase):

    def set_login(self, message: str):
        self.is_present(AuthLocators.LOGIN).send_keys(message)

    def set_password(self, message: str):
        self.is_present(AuthLocators.PASSWORD).send_keys(message)

    def click_sign_in(self):
        self.is_present(AuthLocators.BUTTON_SIGN_IN).click()

