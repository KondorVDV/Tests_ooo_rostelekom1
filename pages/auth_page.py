from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthPage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://b2c.passport.rt.ru'


    def load_auth_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))

    def load_element(self, locator, time=10):
        try:
            WebDriverWait(self.driver, time).until(EC.visibility_of_element_located(locator))
            return True
        except:
            return False


