import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base
from utilities.logger import Logger


class Login_page(Base):
    url = 'https://1001puzzle.ru/'

    # locators
    enter_to_shop = "Вход"
    main_page = "//img[@src='https://1001puzzle.ru/bitrix/templates/1001puzzle/img/logo.png']"
    user_name = "//input[@name='LOGIN']"
    password = "//input[@name='PASSWORD']"
    login_button = "//*[@id='bx_1547235618_kdf8Cm_form']/div[5]/button"
    main_word2 = "//*[@id='sidebarleft']/div/ul/li[2]/a"
    main_word = "//p[@class='client-email']"

    # Getters

    def get_enter_to_shop(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.LINK_TEXT, self.enter_to_shop)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.login_button)))

    def get_go_to_main_page(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_page)))

    def get_main_word(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word)))

    def get_main_word2(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.main_word2)))

    # Actions

    def click_enter_button(self):
        self.get_enter_to_shop().click()
        print("Click login button")

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("Input username")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Input password")

    def click_login_button(self):
        self.get_login_button().click()
        print("Click login button")

    def click_logo(self):
        self.get_go_to_main_page().click()
        print("Click login button")

    # Methods

    def authorization(self):
        with allure.step("authorization"):
            Logger.add_start_step(method='authorization')
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_enter_button()
            self.input_user_name("xxxxx@gmail.com")
            self.input_password("123456")
            self.click_login_button()
            self.get_assert_word(self.get_main_word(), "xxxxx@gmail.com")
            self.get_assert_word(self.get_main_word2(), "Личные данные")
            self.get_go_to_main_page()
            Logger.add_end_step(url=self.driver.current_url, method='authorization')
