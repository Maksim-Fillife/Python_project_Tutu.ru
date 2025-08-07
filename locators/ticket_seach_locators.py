from selenium.webdriver.common.by import By


class TicketSearchLocators:
    INPUT_FROM = (By.XPATH, "//span[@data-ti='input-label'][text()='Откуда']")
    INPUT_TO = (By.XPATH, "//span[@data-ti='input-label'][text()='Куда']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-ti='submit-button']")