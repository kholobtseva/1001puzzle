import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.cart_page import Cart_page
from pages.client_information_page import Cient_information_page
from pages.finish_page import Finish_page
from pages.main_page import Main_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options
from pages.payment_page import Payment_page


@pytest.mark.run(order=2)
def test_by_product_1(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print('Start test by product 1')
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product1()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print("Finish test by product 1")
    driver.quit()


@pytest.mark.run(order=1)
def test_by_product_2(set_group, set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print('Start test by product 2')
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product2()

    cp = Cart_page(driver)
    cp.click_checkout_button()

    print("Finish test by product 2")
    driver.quit()


@pytest.mark.run(order=3)
@allure.description("Test by product")
def test_by_product_3(set_up):
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print('Start test by product 3')
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product3()

    cp = Cart_page(driver)
    cp.get_total_price()
    cp.click_checkout_button()
    cip = Cient_information_page(driver)
    cip.input_information()

    p = Payment_page(driver)
    p.payment()

    f = Finish_page(driver)
    f.finish()

    driver.execute_script("window.history.go(-1)")
    driver.find_element(By.XPATH, "//*[@id='contentid']/form[1]/button").click()


    print("Finish test by_product 3")
    driver.quit()




