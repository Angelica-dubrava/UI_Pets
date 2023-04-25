from pages.login_page import LoginPage, EditPet, DeletePet


def test_go_to_login(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    browser.save_screenshot('res6.png')


def test_go_to_edit(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    link = 'http://34.141.58.52:8080/#/profile'
    page = EditPet(browser, link)
    page.go_to_edit()
    browser.save_screenshot('res9.png')


def test_go_to_delete(browser):
    link = 'http://34.141.58.52:8080/#/login'
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login()
    page.go_to_password()
    page.go_to_button()
    link = 'http://34.141.58.52:8080/#/profile'
    page = DeletePet(browser, link)
    page.go_to_delete()
    page.go_to_delete_yes()
    browser.save_screenshot('res10.png')