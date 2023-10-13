import allure
from selenium.common import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Cient_information_page(Base):


    # locators

    confirm_address = "//*[@id='bx-soa-region']/div[2]/div[3]/div/a"
    delivery_type = "//div[@id='bx-soa-delivery']/div[2]/div[2]/div[1]/div[2]/div[1]"
    confirm_delivery = "//*[@id='bx-soa-delivery']/div[2]/div[3]/div/a[2]"
    paysystem_type = "//*[@id='bx-soa-paysystem']/div[2]/div[2]/div[1]/div[3]/div"
    confirm_type_of_paysystem = "//*[@id='bx-soa-paysystem']/div[2]/div[3]/div/a[2]"
    phone_number = "//input[@id='soa-property-3']"
    address_delivery = "//input[@id='soa-property-7']"
    confirm_personal_information = "//*[@id='bx-soa-properties']/div[2]/div[3]/div/a[2]"
    go_to_cart = "//*[@id='bx_basket1']/a"

    # Getters


    def get_confirm_address(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_address)))

    def get_delivery_type(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.delivery_type)))

    def get_confirm_delivery(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_delivery)))

    def get_paysystem_type(self):
        return WebDriverWait(self.driver,30).until(EC.element_to_be_clickable((By.XPATH, self.paysystem_type)))

    def get_confirm_type_of_paysystem(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_type_of_paysystem)))

    def get_phone_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone_number)))

    def get_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.address_delivery)))

    def get_confirm_personal_information(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.confirm_personal_information)))

    def get_go_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.go_to_cart)))

    #Actions


    def click_confirm_address(self):
        self.get_confirm_address().click()
        print("Click confirm address button")

    def click_delivery_type(self):
        self.get_delivery_type().click()
        print("Click delivery type")

    def click_confirm_delivery(self):
        self.get_confirm_delivery().click()
        print("Click confirm delivery")

    def click_type_of_paysystem(self):
        self.get_paysystem_type().click()
        print("Click type of paysystem")

    def click_confirm_type_of_paysystem(self):
        self.get_confirm_type_of_paysystem().click()
        print("Click confirm type of paysystem")

    def input_phone_number(self,phone_number):
        self.get_phone_number().send_keys(phone_number)
        print("Input phone number")

    def input_delivery_address(self,delivery_address):
        self.get_delivery_address().send_keys(delivery_address)
        print("Input delivery address")

    def click_confirm_personal_information(self):
        self.get_confirm_personal_information().click()
        print("Confirm personal information")

    def click_go_to_cart(self):
        self.get_go_to_cart().click()
        print("Click go to Cart")

    # Methods

    def input_information(self):
        with allure.step("Input information"):
            Logger.add_start_step(method='input_information')

            for _ in range(4):
                try:
                    self.click_confirm_address()
                    self.click_delivery_type()
                    self.click_confirm_delivery()
                    self.click_type_of_paysystem()
                    self.click_confirm_type_of_paysystem()
                    self.input_phone_number("79935026482")
                    self.input_delivery_address("г. Ногинск, ул. Декабристов, 17")
                    self.click_confirm_personal_information()
                except TimeoutException:
                    self.driver.refresh()
                else:
                    break

            Logger.add_end_step(url=self.driver.current_url, method='input_information')

