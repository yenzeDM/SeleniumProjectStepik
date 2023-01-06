from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BUSKET_LINK = (
        By.CSS_SELECTOR, "#default > header > div.page_inner > div > div.basket-mini.pull-right.hidden-xs > span > a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    MESSAGE_ABOUT_BASKET_EMPTY = (
        By.CSS_SELECTOR, "#content_inner > p")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")
    ENTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    ENTER_PASSWORD_ONE = (By.CSS_SELECTOR, "#id_registration-password1")
    ENTER_PASSWOR_TWO = (By.CSS_SELECTOR, "#id_registration-password2")
    SUBMIT_REGISTER = (By.CSS_SELECTOR, "#register_form > button")


class ProductPageLocators:
    SUBMIT_BASKET = (
        By.CSS_SELECTOR, ".btn.btn-lg.btn-primary.btn-add-to-basket")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    MESSAGE_ABOUT_ADDING_NAME_PRODUCT_TO_BASKET = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-success.fade.in .alertinner strong")
    MESSAGE_ABOUT_CASH_VALUE_BASKET = (
        By.CSS_SELECTOR, ".alert.alert-safe.alert-noicon.alert-info.fade.in .alertinner strong")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
