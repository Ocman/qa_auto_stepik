from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import BaseWebDriver
class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM= (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    ADD_TO_CART_BUTTON= (By.CSS_SELECTOR, "#add_to_basket_form .btn-add-to-basket")
    PRODUCT_NAME_IN_PRODUCT_PAGE=(By.CSS_SELECTOR, ".product_main>h1")
    PRODUCT_NAME_IN_HINT = (By.CSS_SELECTOR, "#messages :nth-child(1) .alertinner>strong")
    PRODUCT_PRICE_IN_PRODUCT_PAGE=(By.CSS_SELECTOR, ".product_main .price_color")
    PRODUCT_PRICE_IN_HINT=(By.CSS_SELECTOR, "#messages  .alertinner :nth-child(1) strong")
