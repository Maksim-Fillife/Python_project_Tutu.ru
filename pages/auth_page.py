from locators.auth_locators import AuthLocators as locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.tutu.ru/")

    def open_authorization_page(self):
        enter_button = self.driver.find_element(locator.BTN_ENTER)
        enter_button.click()

    def fill_email(self, email):
        email_box = self.driver.find_element(locator.INPUT_EMAIL)
        email_box.send_keys(email)

    def login_with_password(self):
        password_button = self.driver.find_element(locator.BTN_SWITCH_TO_PASSWORD)
        password_button.click()

    def fill_password(self, password):
        password_box = self.driver.find_element(locator.INPUT_PASSWORD)
        password_box.send_keys(password)

    def fill_wrong_password(self, wr_pas):
        password_box = self.driver.find_element(locator.INPUT_PASSWORD)
        password_box.send_keys(wr_pas)

    def submit_authorization(self):
        submit_authorization = self.driver.find_element(locator.BTN_SUBMIT_LOGIN)
        submit_authorization.click()

    def open_menu(self):
        open_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator.BTN_MENU))
        open_menu.click()

    def check_successful_authorization(self):
        check_successful_authorization = self.driver.find_element(locator.AUTH_SUCCESS)
        assert check_successful_authorization.is_displayed()

    def check_message_auth_error(self):
        auth_error = self.driver.find_element(locator.AUTH_ERROR_MESSAGE)
        assert auth_error.is_displayed()
