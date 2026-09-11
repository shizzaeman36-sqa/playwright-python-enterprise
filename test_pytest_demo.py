from playwright.sync_api import Page, expect
from login_page import LoginPage

# Pytest khud hi 'page' fixture inject kar deta hai
def test_valid_login(page: Page):
    login_p = LoginPage(page)
    
    # 1. Action
    login_p.navigate()
    login_p.login("standard_user", "secret_sauce")
    
    # 2. Web-First Assertion
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_invalid_login(page: Page):
    login_p = LoginPage(page)
    
    # 1. Action
    login_p.navigate()
    login_p.login("invalid_user", "wrong_password")
    
    # 2. Assertion: Error message verify karna
    error_msg = page.locator("[data-test='error']")
    expect(error_msg).to_be_visible()