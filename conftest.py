import pytest
from selenium import webdriver
from pages.auth_page import AuthPage
from pages.catalog_auth_page import Catalog


@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture(scope="module")
def auth_page(driver):
    auth_page = AuthPage(driver)
    return auth_page


@pytest.fixture(scope="module")
def catalog(driver):
    catalog = Catalog(driver)
    return catalog
