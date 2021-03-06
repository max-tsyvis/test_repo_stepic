from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REG_FORM = (By.CSS_SELECTOR,"#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    TOTAL_COUNT_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
    BOOK_NAME = 'The shellcoder\'s handbook'