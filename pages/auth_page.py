import allure

class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.tutu.ru/")