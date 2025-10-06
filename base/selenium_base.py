from typing import List, Tuple
from selenium.common import StaleElementReferenceException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:

    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(self.driver, 10, 0.3, ignored_exceptions=[StaleElementReferenceException])

    def is_present(self, locator: Tuple[str, str]) -> WebElement:
        """
        Ожидание проверки присутствия элемента в DOM страницы.
        # todo
        :param locator: Кортеж в формате (Поиск по, адресс элемента)
        :return:
        """
        return self.__wait.until(ec.presence_of_element_located(locator))

    def are_present(self, locator: Tuple[str, str]) -> List[WebElement]:
        """
        Ожидание проверки наличия на веб-странице списка элементов.
        # todo
        :param locator: Кортеж в формате (Поиск по, адресс элемента)
        :return:
        """
        return self.__wait.until(ec.presence_of_all_elements_located(locator))

    def is_visible(self, locator: Tuple[str, str]) -> WebElement:
        pass


    def are_visible(self, locator: Tuple[str, str]) -> WebElement:
        pass
