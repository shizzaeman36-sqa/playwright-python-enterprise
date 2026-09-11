from playwright.sync_api import sync_playwright

def run_with_saved_state():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)

        # YAHAN MAGIC HAI: Saved state.json file pass kar rahe hain
        context = browser.new_context(storage_state="state.json")
        page = context.new_page()

        # Hum login page par NAHI ja rahe, SEEDHA inventory page khol rahe hain!
        page.goto("https://www.saucedemo.com/inventory.html")

        print("Current Page Title:", page.title())
        print("Current URL:", page.url)

        # Proof ke liye screenshot
        page.screenshot(path="dashboard_without_login.png")

        browser.close()

if __name__ == "__main__":
    run_with_saved_state()