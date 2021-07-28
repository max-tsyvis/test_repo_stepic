from .pages.locators import ProductPageLocators
from .pages.product_page import ProductPage

def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    book_cost = '9.99'
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart()
    product_page.should_be_success_message(ProductPageLocators.BOOK_NAME)
    product_page.should_be_total_amount(book_cost)
