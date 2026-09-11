from playwright.sync_api import sync_playwright, expect
from login_page import LoginPage

def test_saucedemo_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=600)
        page = browser.new_page()

        # Page Object Class initialize kar rahe hain
        login_p = LoginPage(page)

        # Actions perform kar rahe hain
        login_p.navigate()
        login_p.login("standard_user", "secret_sauce")

        # Assertion
        expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
        print("POM Test Passed Successfully!")

        browser.close()

if __name__ == "__main__":
    test_saucedemo_login()