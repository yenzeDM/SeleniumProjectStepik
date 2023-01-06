from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        login_url = self.browser.current_url
        assert 'login' in str(login_url), 'Url have not word "login"'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM), 'Register form is not presented'

    def register_new_user(self, email, password):
        line_email = self.find_element(*LoginPageLocators.ENTER_EMAIL)
        line_email.send_keys(email)
        line_password = self.find_element(
            *LoginPageLocators.ENTER_PASSWORD_ONE)
        line_password.send_keys(password)
        line_password_two = self.find_element(
            *LoginPageLocators.ENTER_PASSWOR_TWO)
        line_password_two.send_keys(password)
        submit_register = self.find_element(*LoginPageLocators.SUBMIT_REGISTER)
        submit_register.click()
