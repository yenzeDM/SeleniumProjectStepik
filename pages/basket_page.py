from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_backet_empty(self):
        assert self.is_element_present(
            *BasketPageLocators.MESSAGE_ABOUT_BASKET_EMPTY), "Message about basket empty is not presented"
