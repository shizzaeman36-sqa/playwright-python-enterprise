from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        # Chromium browser launch kar rahe hain (headless=False se browser screen par dikhega)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # New isolated context aur page create kar rahe hain
        context = browser.new_context()
        page = context.new_page()
        
        # Target site open kar rahe hain
        page.goto("https://www.saucedemo.com")
        
        # Form fill kar rahe hain (User-friendly locators)
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        
        # Login button click kar rahe hain
        page.get_by_text("Login").click()
        
        # Console output verify kar rahe hain
        print("Page Title:", page.title())
        print("Current URL:", page.url)
        
        # Proof ke liye screenshot save kar rahe hain
        page.screenshot(path="login_result.png")
        
        browser.close()

if __name__ == "__main__":
    run()