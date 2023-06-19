from setting import *
from time import sleep

'''Проверка возможности перехода на страницу авторизации ООО «РТК ИТ»'''


def test_load_page_pt001(driver, auth_page, catalog):
    auth_page.load_auth_page()
    title = catalog.get_title_auth_page()
    assert title == "Авторизация"

    # assert auth_page.load_page()


'''Проверка наличия Продуктового слогана ЛК "Ростелеком ID": "Персональный помощник в цифровом мире Ростелекома"'''


def test_load_product_slogan_pt002(driver, auth_page, catalog):
    auth_page.load_auth_page()
    slogan = catalog.get_produсt_slogan()
    assert slogan == "Персональный помощник в цифровом мире Ростелекома"


'''Убеждаемся, что в футере страницы авторизации присутствует номер службы поддержки: 8 800 100 0 800'''


def test_load_support_phone_pt003(driver, auth_page, catalog):
    auth_page.load_auth_page()
    produсt_phone = catalog.get_support_phone()
    assert produсt_phone == "8 800 100 0 800"


'''Убеждаемся, что в правом блоке на странице авторизации присутствует кнопка авторизации через "Вконтакте"'''


def test_load_button_vk_pt004(driver, auth_page, catalog):
    auth_page.load_auth_page()
    assert catalog.load_button_vk()


'''Убеждаемся, что в правом блоке на странице авторизации присутствует кнопка авторизации через "Однокласники"'''


def test_load_button_ok_pt005(driver, auth_page, catalog):
    auth_page.load_auth_page()
    assert catalog.load_button_ok()


'''Убеждаемся, что в правом блоке на странице авторизации присутствует кнопка авторизации через "Mail.ru"'''


def test_load_button_mail_pt006(driver, auth_page, catalog):
    auth_page.load_auth_page()
    assert catalog.load_button_mail()


'''Убеждаемся, что в правом блоке на странице авторизации присутствует кнопка авторизации через "Yandex"'''


def test_load_button_ya_pt007(driver, auth_page, catalog):
    auth_page.load_auth_page()
    assert catalog.load_button_ya()


'''Проверяем возможность авторизации по номеру телефона и паролю'''


def test_auth_phone_nuber_pt008(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_tab_phone()
    catalog.clear_element_input_username()
    catalog.input_element_input_user_phone(user_phone)
    catalog.input_element_input_password(password)
    catalog.click_button_come_in()
    assert catalog.load_personal_area()
    catalog.click_button_exit()


'''Проверяем возможность авторизации по почте и паролю'''


def test_auth_mail_pt009(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_tab_mail()
    catalog.clear_element_input_username()
    catalog.input_element_input_user_email(user_email)
    catalog.input_element_input_password(password)
    catalog.click_button_come_in()
    assert catalog.load_personal_area()
    catalog.click_button_exit()


'''Проверяем возможность авторизации по логину и паролю'''


def test_auth_login_pt010(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_tab_login()
    catalog.clear_element_input_username()
    catalog.input_element_input_user_login(user_login)
    catalog.input_element_input_password(password)
    catalog.click_button_come_in()
    assert catalog.load_personal_area()
    catalog.click_button_exit()


'''Проверяем возможность авторизации по лицевому счету и паролю'''


def test_auth_personal_account_pt011(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_tab_ls()
    catalog.clear_element_input_username()
    catalog.input_element_input_Personal_account(user_personal_account)
    catalog.input_element_input_password(password)
    catalog.click_button_come_in()
    assert catalog.load_personal_area()
    catalog.click_button_exit()


'''Возможность авторизации по кнопке соц сети  "Вконтакте"'''


def test_auth_vk_pt012(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_vk()
    vk = catalog.get_title_vk()
    assert vk == "VK ID"


'''Возможность авторизации по кнопке соц сети  "Одноклассники"'''


def test_auth_ya_pt013(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_ok()
    ok = catalog.get_title_ok()
    assert ok == "Одноклассники"


'''Возможность авторизации по кнопке соц сети  "MAil.ru"'''


def test_auth_ya_pt014(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_mail()
    mail = catalog.get_title_mail()
    assert mail == "Mail.Ru — Запрос доступа"


'''Возможность авторизации по кнопке соц сети  "Яндекс"'''


def test_auth_ya_pt015(driver, auth_page, catalog):
    auth_page.load_auth_page()
    catalog.click_button_ya()
    ya = catalog.get_title_ya()
    assert ya == "Доступ внешних приложений"
