from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()

        # -------------------------------------------------------------
        # SCENARIO 1: MOUSE HOVER
        # -------------------------------------------------------------
        page.goto("https://the-internet.herokuapp.com/hovers")

        # First avatar (image) par mouse hover karte hain
        first_avatar = page.locator(".figure").first
        first_avatar.hover()

        # Hover hone ke baad jo text dikhta hai usko verify karte hain
        expect(page.get_by_text("name: user1")).to_be_visible()
        print("Mouse Hover Passed!")


        # -------------------------------------------------------------
        # SCENARIO 2: DRAG AND DROP
        # -------------------------------------------------------------
        page.goto("https://the-internet.herokuapp.com/drag_and_drop")

        # Box A ko Drag karke Box B par Drop karna
        source_box = page.locator("#column-a")
        target_box = page.locator("#column-b")

        # Direct Playwright drag_to method
        source_box.drag_to(target_box)

        # Check karte hain ke Column A mein ab "B" aa chuka hai
        expect(source_box).to_have_text("B")
        print("Drag and Drop Passed!")

        browser.close()

if __name__ == "__main__":
    run()