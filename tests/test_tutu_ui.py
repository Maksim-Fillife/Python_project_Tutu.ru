from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import dotenv
dotenv.load_dotenv()


def test_valid_authorization(driver):
    driver.get("https://www.tutu.ru/")
    enter_button = driver.find_element(By.XPATH, "//span[text()='Войти']")
    enter_button.click()
    email_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='email-or-phone-field']")
    email_box.send_keys(email)
    password_button = driver.find_element(By.CSS_SELECTOR, "button[data-ti='login-by-password-trigger']")
    password_button.click()
    password_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='password-field']")
    password_box.send_keys(password)
    submit_authorization = driver.find_element(By.CSS_SELECTOR, "button[data-ti='submit-trigger']")
    submit_authorization.click()
    open_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Открыть меню']")))
    open_menu.click()
    check_successful_authorization = driver.find_element(By.CSS_SELECTOR, "span[data-ti='email']")
    assert check_successful_authorization.is_displayed()

def test_logout(driver):
    driver.get("https://www.tutu.ru/")
    enter_btn = driver.find_element(By.XPATH, "//span[text()='Войти']")
    enter_btn.click()
    email_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='email-or-phone-field']")
    email_box.send_keys(email)
    password_button = driver.find_element(By.CSS_SELECTOR, "button[data-ti='login-by-password-trigger']")
    password_button.click()
    password_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='password-field']")
    password_box.send_keys(password)
    submit_authorization = driver.find_element(By.CSS_SELECTOR, "button[data-ti='submit-trigger']")
    submit_authorization.click()
    open_menu = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[aria-label='Открыть меню']")))
    open_menu.click()
    check_successful_authorization = driver.find_element(By.CSS_SELECTOR, "span[data-ti='email']")
    check_successful_authorization.is_displayed()
    btn_logout = driver.find_element(By.XPATH, "//span[@data-ti='label-value-label' and text()='Выйти']")
    btn_logout.click()
    check_logout = driver.find_element(By.XPATH, "//span[text()='Войти']")
    assert check_logout.is_displayed()

def test_login_with_wrong_password(driver):
    driver.get("https://www.tutu.ru/")
    enter_btn = driver.find_element(By.XPATH, "//span[text()='Войти']")
    enter_btn.click()
    email_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='email-or-phone-field']")
    email_box.send_keys(email)
    password_button = driver.find_element(By.CSS_SELECTOR, "button[data-ti='login-by-password-trigger']")
    password_button.click()
    password_box = driver.find_element(By.CSS_SELECTOR, "input[data-ti='password-field']")
    password_box.send_keys(wr_pass)
    submit_authorization = driver.find_element(By.CSS_SELECTOR, "button[data-ti='submit-trigger']")
    submit_authorization.click()
    message_error = driver.find_element(By.XPATH, "//p[@data-ti-error='authApi']")
    assert message_error.is_displayed()