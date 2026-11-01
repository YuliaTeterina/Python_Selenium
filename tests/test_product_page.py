
import pytest

from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):

    link = (
        "http://selenium1py.pythonanywhere.com/"
        "catalogue/coders-at-work_207/"
        "?promo=newYear2019"
    )

    page = ProductPage(browser, link)

    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()

    page.solve_quiz_and_get_code()

    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)
