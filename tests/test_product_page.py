
import pytest

from pages.product_page import ProductPage



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

def test_guest_can_add_product_to_basket(browser, offer):
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
