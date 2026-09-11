from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()

        # Shadow DOM wali practice site
        page.goto("https://the-internet.herokuapp.com/shadowdom")

        # Page par Shadow Root ke andar maujood text element ko direct get_by_text se target kar rahe hain
        shadow_text = page.get_by_text("Let's have some different text!")

        # Verify karte hain ke Playwright ne Shadow DOM ke andar se text padh liya
        expect(shadow_text).to_be_visible()
        print("Shadow DOM Text Found:", shadow_text.text_content())

        browser.close()

if __name__ == "__main__":
    run()