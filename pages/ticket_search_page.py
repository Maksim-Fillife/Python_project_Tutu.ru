from locators.ticket_seach_locators import TicketSearchLocators as locator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class TicketSearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.tutu.ru/")

    def bus_ticket(self):
        bus_ticket = self.wait.until(
            EC.visibility_of_element_located(locator.BUSS_TICKET)
        )
        bus_ticket.click()

    def set_route(self, from_city='Москва', to_city='Санкт-Петербург'):
        from_input = self.wait.until(
            EC.element_to_be_clickable(locator.INPUT_FROM)
        )
        from_input.clear()
        from_input.send_keys(from_city)

        from_to = self.wait.until(
            EC.element_to_be_clickable(locator.INPUT_TO)
        )
        from_to.clear()
        from_to.send_keys(to_city)