from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class Driver:

    def get_webdriver(self):
        options =  Options()
        options.add_argument("--headless")  # Новый headless режим
        options.add_argument("--no-sandbox")

        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1280, 1024)
        driver.implicitly_wait(3)
        driver.get("https://intuit.ru/")

        return driver
