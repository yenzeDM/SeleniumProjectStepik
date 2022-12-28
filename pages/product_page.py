from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_submit_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.SUBMIT_BASKET)

    def add_to_basket(self):
        find_submit_basket = self.find_element(
            *ProductPageLocators.SUBMIT_BASKET)
        find_submit_basket.click()
        self.solve_quiz_and_get_code()

    def message_coincide_with_name_product(self):
        message = self.find_element(
            *ProductPageLocators.MESSAGE_ADD_NAME_PRODUCT_TO_BASKET)
        name_product = self.find_element(*ProductPageLocators.NAME_PRODUCT)
        assert message.text == name_product.text, 'Message about add to basket has not correct name product'

    def message_price_coincide_with_price_product(self):
        price_message = self.find_element(
            *ProductPageLocators.MESSAGE_ABOUT_CASH_VALUE_BASKET)
        price_product = self.find_element(*ProductPageLocators.PRICE_PRODUCT)
        assert price_message.text == price_product.text, 'Message about cash value basket does not coincide with price product'
