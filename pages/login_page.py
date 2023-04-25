import time

import pytest

from .base_page import BasePage
from .locators import LoginPageLocators, EditPetLocators, DeletePetLocators


class LoginPage(BasePage):

    @pytest.mark.regression
    def go_to_login(self):
        login_email = self.browser.find_element(*LoginPageLocators.LOGIN_EMAIL)
        login_email.send_keys('ang.dubrava@gmail.com')

    @pytest.mark.regression
    def go_to_password(self):
        login_password = self.browser.find_element(*LoginPageLocators.LOGIN_PASS)
        login_password.send_keys('Way1234!')

    @pytest.mark.regression
    def go_to_button(self):
        login_button = self.browser.find_element(*LoginPageLocators.LOGIN_BTN)
        login_button.submit()
        time.sleep(2)


class EditPet(BasePage):

    @pytest.mark.smoke
    def go_to_edit(self):
        edit_pet = self.browser.find_element(*EditPetLocators.PET_EDIT)
        edit_pet.click()
        time.sleep(2)


class DeletePet(BasePage):

    @pytest.mark.smoke
    def go_to_delete(self):
        delete_pet = self.browser.find_element(*DeletePetLocators.PET_DELETE)
        delete_pet.click()

    def go_to_delete_yes(self):
        delete_pet_yes = self.browser.find_element(*DeletePetLocators.PET_DELETE_YES)
        delete_pet_yes.click()
