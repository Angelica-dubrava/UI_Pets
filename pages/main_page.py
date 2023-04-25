import time

import pytest

from .locators import MainPageLocators, DetailsPageLocators, MainDropDownPageLocators
from .base_page import BasePage


class MainPage(BasePage):

    @pytest.mark.regression
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()


class DetailsPage(BasePage):

    @pytest.mark.smoke
    def go_to_details(self):
        details_link = self.browser.find_element(*DetailsPageLocators.DETAILS)
        details_link.click()


class DropdownPage(BasePage):
    def go_to_dropdown(self):
        dropdown_arrow = self.browser.find_element(*MainDropDownPageLocators.DROPDOWN)
        dropdown_arrow.click()

    def go_to_animal(self):
        dropdown_animal = self.browser.find_element(*MainDropDownPageLocators.DROPDOWN_ANIMAL)
        dropdown_animal.click()
        time.sleep(2)
