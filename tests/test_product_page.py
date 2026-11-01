
import pytest

from pages.product_page import ProductPage


# Задания 1 и 2
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"

    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)


# Задание 3
@pytest.mark.parametrize(
    "offer",
    [
        "offer0",
        "offer1",
        "offer2",
        "offer3",
        "offer4",
        "offer5",
        "offer6",
        pytest.param(
            "offer7",
            marks=pytest.mark.xfail(reason="Bug in offer7")
        ),
        "offer8",
        "offer9"
    ]
)
def test_guest_can_add_product_to_basket_with_promo(browser, offer):
    link = (
        "http://selenium1py.pythonanywhere.com/"
        f"catalogue/coders-at-work_207/?promo={offer}"
    )

    page = ProductPage(browser, link)
    page.open()

    product_name = page.get_product_name()
    product_price = page.get_product_price()

    page.add_product_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_success_message(product_name)
    page.should_be_basket_total(product_price)


# Задание 4. Тест 1
@pytest.mark.xfail(
    reason="Success message appears after adding product"
)
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    assert page.is_not_element_present(
        *page.SUCCESS_MESSAGE
    ), "Success message is presented, but should not be"


# Задание 4. Тест 2
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()

    assert page.is_not_element_present(
        *page.SUCCESS_MESSAGE
    ), "Success message is presented, but should not be"


# Задание 4. Тест 3
@pytest.mark.xfail(
    reason="Success message does not disappear"
)
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    assert page.is_disappeared(
        *page.SUCCESS_MESSAGE
    ), "Success message did not disappear"
