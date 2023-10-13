import datetime

from selenium.common import TimeoutException


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url: " + get_url)

    """Method assert word"""

    def get_assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(value_word)
        print("Good value word.")

    """Method screen shot"""

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot(name_screenshot)
        print("Get screenshot")

    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        try:
            assert get_url == result
            print("Good value url.")
        except TimeoutException:
            print("!!!Bad value url!!!")

    """Method assert price"""

    def assert_price(self, product_price, result):
        try:
            assert product_price.text == result
            print("Good value product price")
        except TimeoutException:
            print("!!!Bad value product price!!!")
