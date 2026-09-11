from playwright.sync_api import sync_playwright

def save_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # Login process
        page.goto("https://www.saucedemo.com")
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Login hone ke baad session cookies ko json file mein save kar rahe hain
        context.storage_state(path="state.json")
        print("Login Session successfully saved to state.json!")

        browser.close()

if __name__ == "__main__":
    save_state()