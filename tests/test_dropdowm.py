from pages.main_page import DropdownPage


def test_go_to_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = DropdownPage(browser, link)
    page.open()
    page.go_to_dropdown()
    page.go_to_animal()
    browser.save_screenshot('res7.png')
