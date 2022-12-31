from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, ".col-sm-6.login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, ".col-sm-6.register_form")


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
