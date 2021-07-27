from .base_page import BasePage
import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click() 

    def should_be_login_link(self):
        assert self.if_elememt_present(By.CSS_SELECTOR,"#login_link"), "Login link is not presented"