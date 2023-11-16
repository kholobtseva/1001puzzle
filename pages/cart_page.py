import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cart_page(Base):

    # locators
    checkout = "//*[@id='basket_items_list']/div[2]/div[4]/a"
    total_price = "//*[@id='allSum_FORMATED']"

    # Getters

    def get_checkout(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkout)))

    def get_total_price(self):
        price_in_cart = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))
        self.assert_price(price_in_cart, "4 223 р.")
        print("Total price with delivery", price_in_cart.text)

    # Actions

    def click_checkout_button(self):
        self.get_checkout().click()
        print("Click checkout button")

    # Methods

    def product_confirmation(self):
        with allure.step("product_confirmation"):
            Logger.add_start_step(method='product_confirmation')
            self.get_current_url()
            self.click_checkout_button()
            Logger.add_end_step(url=self.driver.current_url, method='product_confirmation')