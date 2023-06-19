from selenium.webdriver.common.by import By
from pages.auth_page import AuthPage


class Catalog(AuthPage):
    LOCATOR_AUTH_PAGE_TITLE = (By.CLASS_NAME, 'card-container__title')
    LOCATOR_PRODUCT_SLOGAN = (By.CLASS_NAME, 'what-is__desc')
    LOCATOR_SUPPORT_PHONE = (By.CLASS_NAME, 'rt-footer-right__support-phone')
    LOCATOR_BUTTON_VK = (By.ID, "oidc_vk")
    LOCATOR_BUTTON_OK = (By.ID, "oidc_ok")
    LOCATOR_BUTTON_MAIL = (By.ID, "oidc_mail")
    LOCATOR_BUTTON_YA = (By.ID, "oidc_ya")
    LOCATOR_BUTTON_TAB_PHONE = (By.ID, "t-btn-tab-phone")
    LOCATOR_BUTTON_TAB_MAIL = (By.ID, "t-btn-tab-mail")
    LOCATOR_BUTTON_TAB_LOGIN = (By.ID, "t-btn-tab-login")
    LOCATOR_BUTTON_TAB_LS = (By.ID, "t-btn-tab-ls")
    LOCATOR_BUTTON_COM_IN = (By.ID, "kc-login")
    LOCATOR_INPUT_USERNAME = (By.ID, "username")
    LOCATOR_INPUT_PASSWORD = (By.ID, "password")
    LOCATOR_USER_NAME = (By.CLASS_NAME, "user-name__first-patronymic")
    LOCATOR_BUTTON_EXIT = (By.ID, "logout-btn")
    LOCATOR_TITLE_VK = (By.XPATH, '/html/head/title')
    LOCATOR_TITLE_OK = (By.XPATH, '/html/head/title')
    LOCATOR_TITLE_MAIL = (By.XPATH, '/html/head/title')
    LOCATOR_TITLE_YA = (By.XPATH, '/html/head/title')


    def get_title_auth_page(self):
        return self.find_element(self.LOCATOR_AUTH_PAGE_TITLE).text

    def get_produсt_slogan(self):
        return self.find_element(self.LOCATOR_PRODUCT_SLOGAN).text

    def get_support_phone(self):
        return self.find_element(self.LOCATOR_SUPPORT_PHONE).text

    def load_button_vk(self):
        return self.load_element(self.LOCATOR_BUTTON_VK)

    def load_button_ok(self):
        return self.load_element(self.LOCATOR_BUTTON_OK)

    def load_button_mail(self):
        return self.load_element(self.LOCATOR_BUTTON_MAIL)

    def load_button_ya(self):
        return self.load_element(self.LOCATOR_BUTTON_YA)

    def click_button_tab_phone(self):
        return self.find_element(self.LOCATOR_BUTTON_TAB_PHONE).click()

    def click_button_tab_mail(self):
        return self.find_element(self.LOCATOR_BUTTON_TAB_LOGIN).click()

    def click_button_tab_login(self):
        return self.find_element(self.LOCATOR_BUTTON_TAB_MAIL).click()

    def click_button_tab_ls(self):
        return self.find_element(self.LOCATOR_BUTTON_TAB_LS).click()

    def click_button_come_in(self):
        return self.find_element(self.LOCATOR_BUTTON_COM_IN).click()

    def clear_element_input_username(self):
        return self.find_element(self.LOCATOR_INPUT_USERNAME).clear()

    def clear_element_input_password(self):
        return self.find_element(self.LOCATOR_INPUT_PASSWORD).clear()

    def input_element_input_user_login(self, user_login):
        return self.find_element(self.LOCATOR_INPUT_USERNAME).send_keys(f'{user_login}')

    def input_element_input_Personal_account(self, user_personal_account):
        return self.find_element(self.LOCATOR_INPUT_USERNAME).send_keys(f'{user_personal_account}')

    def input_element_input_user_phone(self, user_phone):
        return self.find_element(self.LOCATOR_INPUT_USERNAME).send_keys(f'{user_phone}')

    def input_element_input_user_email(self, user_email):
        return self.find_element(self.LOCATOR_INPUT_USERNAME).send_keys(f'{user_email}')

    def input_element_input_password(self, password):
        return self.find_element(self.LOCATOR_INPUT_PASSWORD).send_keys(f'{password}')

    def load_personal_area(self):
        return self.load_element(self.LOCATOR_USER_NAME)

    def click_button_exit(self):
        return self.find_element(self.LOCATOR_BUTTON_EXIT).click()

    def click_button_vk(self):
        return self.find_element(self.LOCATOR_BUTTON_VK).click()

    def click_button_ok(self):
        return self.find_element(self.LOCATOR_BUTTON_OK).click()

    def click_button_mail(self):
        return self.find_element(self.LOCATOR_BUTTON_MAIL).click()

    def click_button_ya(self):
        return self.find_element(self.LOCATOR_BUTTON_YA).click()

    def get_title_vk(self):
        return self.find_element(self.LOCATOR_TITLE_VK).text

    def get_title_ok(self):
        return self.find_element(self.LOCATOR_TITLE_OK).text

    def get_title_mail(self):
        return self.find_element(self.LOCATOR_TITLE_MAIL).text

    def get_title_ya(self):
        return self.find_element(self.LOCATOR_TITLE_YA).text












