from .base_page import BasePage
from .locators import ProductPageLocators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class ProductPage(BasePage):
    def add_to_cart(self):
        add_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_button.click()
        self.solve_quiz_and_get_code()

    def should_be_success_message(self, book_title):
        assert self.if_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Book isn't added to cart successfully"
        assert f"{book_title} has been added to your basket." in self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE).text, "That's wrong book"

    def should_be_total_amount(self, book_cost):
        assert self.if_element_present(*ProductPageLocators.TOTAL_COUNT_MESSAGE), "Total amount message didn't apear"
        assert book_cost in self.browser.find_element(*ProductPageLocators.TOTAL_COUNT_MESSAGE).text, "Total ammount is wrong"        

    def get_book_name(self):
        book = self.browser.find_element(By.TAG_NAME,"h1")
        return book.text