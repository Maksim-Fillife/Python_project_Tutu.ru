from selenium.webdriver.common.by import By


class TicketSearchLocators:

    # ---Выбор катигории---
    BUSS_TICKET = (By.XPATH, "//button[.//span[text()='Автобусы']]")
    TRAIN_TICKET = (By.XPATH, "//button[.//span[text()='Ж/д билеты']]")
    AVIA_TICKET = (By.XPATH, "//button[.//span[text()='Авиабилеты']]")

    # ---Поиск билетов---
    INPUT_FROM = (By.XPATH, "//input[@data-ti='input'][following-sibling::span[text()='Откуда']]")
    INPUT_TO = (By.XPATH, "//input[@data-ti='input'][following-sibling::span[text()='Куда']]")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-ti='submit-button']")

    # ---Сортировки---
    SORT_BUTTON = (By.XPATH, "//button[.//span[@data-ti='name_option'][text()='Сортировка']]")
    SORT_FROM_PRICE = (By.XPATH, "//div[contains(@class, 'o-select-selected') and contains(., 'Стоимость')]")