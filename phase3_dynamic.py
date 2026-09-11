from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()

        # Dynamic Loading practice page
        page.goto("https://the-internet.herokuapp.com/dynamic_loading/1")

        # Start Button click karte hain (is ke click se 5 seconds ka delay start hota hai)
        page.get_by_role("button", name="Start").click()

        # Target element jo 5 seconds baad screen par aayega
        finish_text = page.locator("#finish h4")

        # Playwright auto-wait karega default 30s tak. 
        # Hum web-first assertion use karke ensure karenge ke text visible hone ka wait kare
        expect(finish_text).to_be_visible(timeout=10000) # 10 seconds custom timeout

        print("Dynamic Text Loaded Successfully:", finish_text.text_content())

        browser.close()

if __name__ == "__main__":
    run()