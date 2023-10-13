from base.base_class import Base
from utilities.logger import Logger
import allure

class Finish_page(Base):

    # locators

    # Getters

    # Actions

    # Methods

    def finish(self):
        with allure.step("Finish"):
            Logger.add_start_step(method='finish')
            self.get_current_url()
            self.assert_url("https://1001puzzle.ru/personal/order/make/")
            Logger.add_end_step(url=self.driver.current_url, method='finish')
