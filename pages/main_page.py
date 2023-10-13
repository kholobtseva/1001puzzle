import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Main_page(Base):


    name_of_manufacturer = "Пазлы Cobble Hill"

    # locators
    select_product_1 = "//*[@id='bx_3966226736_429381']/div[2]/a/img"
    select_product_2 = "//*[@id='bx_3966226736_429371']/div[2]/a/img"
    select_product_3 = "//*[@id='bx_3966226736_429372']/div[2]/a/img"
    cart = "//a[@href='/personal/cart/']"
    main_catalog_page = "//img[@class='logo-img']"
    manufacturer = "//a[@href='#proizvoditeli']"
    choose_manufacturer = "//a[@href='/pazly/proizvoditeli/cobble-hill/']"
    page_2 = "//a[@href='/pazly/proizvoditeli/cobble-hill/?detaley_list=1_000&puzzle_tema=zhivotnye&PAGEN_1=2']"
    number_of_puzzle = "//input[@id='arrFilter_228_2561098286']"
    category_of_puzzle = "//input[@id='arrFilter_134_2456969798']"
    manuf_text = "//*[@id='contentid']/h1"
    clean_cart_button = "//*[@id='contentid']/form[1]/button"
    useful = "//a[@href='#more']"
    choose_review = "//a[@href='/obzory/']"
    choose_review_description = "//a[@href='/obzory/429295/']"


    # Getters

    def get_select_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_1)))

    def get_select_product_2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_2)))

    def get_select_product_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_product_3)))

    def get_catalog_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_catalog_page)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    def get_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manufacturer)))

    def get_choose_manufacturer(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_manufacturer)))

    def get_manuf_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.manuf_text)))

    def get_choose_number(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.number_of_puzzle)))

    def get_choose_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.category_of_puzzle)))

    def get_page_2(self):
        return WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, self.page_2)))

    def get_clean_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.clean_cart_button)))

    def get_useful_menue(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.useful)))

    def get_choose_review(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_review)))

    def get_review_description(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.choose_review_description)))

    # Actions

    def click_select_product_1(self):
        self.get_select_product_1().click()
        print("Click select product 1 button")

    def click_select_product_2(self):
        self.get_select_product_2().click()
        print("Click select product 2 button")

    def click_select_product_3(self):
        self.get_select_product_3().click()
        print("Click select product 3 button")

    def click_cart(self):
        self.get_cart().click()
        print("Click cart")

    def click_main_page(self):
        self.get_catalog_page().click()
        print("Click logo of the site for getting to the main page")

    def click_manufacturer(self):
        self.get_manufacturer().click()
        print("Click manufacturer menu")

    def click_choose_manufacturer(self):
        self.get_choose_manufacturer().click()
        print("Click choose manufacturer")

    def click_choose_number(self):
        self.get_choose_number().click()
        print("Click choose number of pieces")

    def click_choose_category(self):
        self.get_choose_category().click()
        print("Click choose category")

    def click_page_2(self):
        self.get_page_2().click()
        print("Click page 2")

    def check_manuf_name(self):
        print(self.get_manuf_name().text)
        assert self.get_manuf_name().text == self.name_of_manufacturer
        print("Check manufacturer name is correct!")

    def click_useful_menue(self):
        self.get_useful_menue().click()
        print("Click menu Useful")

    def click_choose_review(self):
        self.get_choose_review().click()
        print("Click Review")

    def click_review_description(self):
        self.get_review_description().click()
        print("Click review content")

    # Methods

    def select_product1(self):
        with allure.step("Select product 1"):
            Logger.add_start_step(method='select_product1')
            self.click_main_page()
            self.get_current_url()
            self.click_manufacturer()
            self.click_choose_manufacturer()
            self.check_manuf_name()
            self.click_choose_number()
            self.click_choose_category()
            self.click_page_2()
            self.click_select_product_1()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_product1')

    def select_product2(self):
        with allure.step("Select product 2"):
            Logger.add_start_step(method='select_product2')
            self.click_main_page()
            self.get_current_url()
            self.click_manufacturer()
            self.click_choose_manufacturer()
            self.check_manuf_name()
            self.click_choose_number()
            self.click_choose_category()
            self.click_page_2()
            self.click_select_product_2()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_product2')

    def select_product3(self):
        with allure.step("Select product 3"):
            Logger.add_start_step(method='select_product3')
            self.click_main_page()
            self.get_current_url()
            self.click_manufacturer()
            self.click_choose_manufacturer()
            self.check_manuf_name()
            self.click_choose_number()
            self.click_choose_category()
            self.click_page_2()
            self.click_select_product_3()
            self.click_cart()
            Logger.add_end_step(url=self.driver.current_url, method='select_product3')

    def select_about_puzzle(self):
        with allure.step("Select about puzzle"):
            Logger.add_start_step(method='select_about_puzzle')
            self.click_main_page()
            self.click_useful_menue()
            self.click_choose_review()
            self.click_review_description()
            self.assert_url("https://1001puzzle.ru/obzory/429295/")
            Logger.add_end_step(url=self.driver.current_url, method='select_about_puzzle')


