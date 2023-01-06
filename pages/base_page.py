from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .locators import BasePageLocators
import math


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, method, css_celector):
        try:
            self.browser.find_element(method, css_celector)
        except NoSuchElementException:
            return False
        return True

    def find_element(self, method, css_celector):
        try:
            return self.browser.find_element(method, css_celector)
        except NoSuchElementException as noelem:
            return noelem

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, method, css_celector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(
                EC.presence_of_element_located((method, css_celector)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, method, css_celector, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException).\
                until_not(EC.presence_of_element_located(
                    (method, css_celector)))
        except TimeoutException:
            return False
        return True

    def go_to_login_page(self):
        link = self.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(
            *BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def go_to_basket_page(self):
        link = self.find_element(*BasePageLocators.BUSKET_LINK)
        link.click()

    def should_be_authorized_user(self):
        assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
            " probably unauthorised user"

    def send_keys(self, data):
        tmp = self.browser.send_keys(data)
