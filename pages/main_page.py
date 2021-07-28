from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage
from .product_page import ProductPage
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.if_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"