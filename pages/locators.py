from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#app > header > div > ul > li:nth-child(1) > a >  span')


class LoginPageLocators:
    LOGIN_EMAIL = (By.ID, "login")
    LOGIN_PASS = (By.XPATH, '//*[@id="password"]/input')
    LOGIN_BTN = (By.CLASS_NAME, "p-button-label")


class MainDropDownPageLocators:
    DROPDOWN = (By.XPATH, '//*[@id="pv_id_2"]/div')
    DROPDOWN_ANIMAL = (By.ID, 'pv_id_2_0')


class DetailsPageLocators:
    DETAILS = (By.XPATH, '//*[@id="app"]/main/div/div[2]/div[2]/div/div[1]/div/div[3]/div[1]/button')


class EditPetLocators:
    PET_EDIT = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div[1]/div/div[2]/button[1]')


class DeletePetLocators:
    PET_DELETE = (By.XPATH, '//*[@id="app"]/main/div/div/div[2]/div/div/div/div[2]/button[2]')
    PET_DELETE_YES = (By.XPATH, '//button[contains(.,"Yes")]')
