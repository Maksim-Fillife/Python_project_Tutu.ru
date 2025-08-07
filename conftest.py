from selenium import webdriver
import dotenv
dotenv.load_dotenv()
import pytest
import os



email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")
wr_pass = os.getenv("WRONG_PASSWORD")

@pytest.fixture()
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()