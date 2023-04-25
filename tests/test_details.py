from pages.main_page import DetailsPage


def test_go_to_dropdown(browser):
    link = 'http://34.141.58.52:8080/#/'
    page = DetailsPage(browser, link)
    page.open()
    page.go_to_details()
    browser.save_screenshot('res8.png')

