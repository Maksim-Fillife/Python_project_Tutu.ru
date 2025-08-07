from selenium import webdriver
import pytest
import os
import dotenv
dotenv.load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def driver():
    browser = webdriver.Firefox()
    browser.maximize_window()
    browser.implicitly_wait(3)
    yield browser
    browser.quit()

@pytest.fixture
def authorization(driver):
    from pages.auth_page import AuthorizationPage as auth
    return auth(driver)

@pytest.fixture(scope='function', autouse=True)
def email():
    return os.getenv("EMAIL")

@pytest.fixture
def password():
    return os.getenv("PASSWORD")

@pytest.fixture
def wr_pass():
    return os.getenv("WRONG_PASSWORD")