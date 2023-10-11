import allure
from selenium import webdriver
from pages.main_page import Main_page
from pages.login_page import Login_page
from selenium.webdriver.chrome.options import Options


@allure.description("Test puzzle review")
def test_puzzle_review():
    options = Options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)

    print('Start test')
    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_about_puzzle()

    print("Finish test")
    driver.quit()
