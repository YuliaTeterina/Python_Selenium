
from selenium.webdriver.common.by import By

from .base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_BASKET_BUTTON = (
        By.CSS_SELECTOR,
        "button.btn-add-to-basket"
    )

    PRODUCT_NAME = (
        By.CSS_SELECTOR,
        "div.product_main h1"
    )

    PRODUCT_PRICE = (
        By.CSS_SELECTOR,
        "p.price_color"
    )

    SUCCESS_MESSAGE = (
        By.CSS_SELECTOR,
        "div.alert-success strong"
    )

    BASKET_TOTAL_MESSAGE = (
        By.CSS_SELECTOR,
        "div.alert-info"
    )

    def add_product_to_basket(self):
        button = self.browser.find_element(
            *self.ADD_TO_BASKET_BUTTON
        )
        button.click()

    def get_product_name(self):
        return self.browser.find_element(
            *self.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *self.PRODUCT_PRICE
        ).text

    def should_be_success_message(self, product_name):
        message = self.browser.find_element(
            *self.SUCCESS_MESSAGE
        ).text

        assert product_name == message

    def should_be_basket_total(self, product_price):
        message = self.browser.find_element(
            *self.BASKET_TOTAL_MESSAGE
        ).text

        assert product_price in message
