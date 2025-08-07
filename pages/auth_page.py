from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import allure

class AuthorizationPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get("https://www.tutu.ru/")

    def open_authorization_page(self):
        enter_button = self.driver.find_element(By.XPATH, "//span[text()='Войти']")
        enter_button.click()

    def fill_email(self, email):
        email_box = self.driver.find_element(By.CSS_SELECTOR, "input[data-ti='email-or-phone-field']")
        email_box.send_keys(email)

    def login_with_password(self):
        password_button = self.driver.find_element(By.CSS_SELECTOR, "button[data-ti='login-by-password-trigger']")
        password_button.click()

    def fill_password(self, password):
        password_box = self.driver.find_element(By.CSS_SELECTOR, "input[data-ti='password-field']")
        password_box.send_keys(password)

    def fill_wrong_password(self, wr_pas):
        password_box = self.driver.find_element(By.CSS_SELECTOR, "input[data-ti='password-field']")
        password_box.send_keys(wr_pas)

    def submit_authorization(self):
        submit_authorization = self.driver.find_element(By.CSS_SELECTOR, "button[data-ti='submit-trigger']")
        submit_authorization.click()

    def open_menu(self):
        open_menu = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Открыть меню']")))
        open_menu.click()

    def check_successful_authorization(self):
        check_successful_authorization = self.driver.find_element(By.CSS_SELECTOR, "span[data-ti='email']")
        assert check_successful_authorization.is_displayed()

    def check_message_auth_error(self):
        auth_error = self.driver.find_element(By.XPATH, "//p[@data-ti-error='authApi']")
        assert auth_error.is_displayed()
