from selenium.webdriver.common.by import By


class AuthLocators:
    # ---Главная страница---
    BTN_ENTER = (By.XPATH, "//span[text()='Войти']")

    # ---Форма входа---
    INPUT_EMAIL = (By.CSS_SELECTOR, "input[data-ti='email-or-phone-field']")
    BTN_SWITCH_TO_PASSWORD = (By.CSS_SELECTOR, "button[data-ti='login-by-password-trigger']")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "input[data-ti='password-field']")
    BTN_SUBMIT_LOGIN = (By.CSS_SELECTOR, "button[data-ti='submit-trigger']")
    AUTH_ERROR_MESSAGE = (By.XPATH, "//p[@data-ti-error='authApi']")

    # ---Меню пользователя---
    BTN_MENU =(By.CSS_SELECTOR, "button[aria-label='Открыть меню']")
    LINK_PROFILE = (By.CSS_SELECTOR, "span[data-ti='email']")
    LINK_LOGOUT = (By.XPATH, "//span[@data-ti='label-value-label' and text()='Выйти']")
