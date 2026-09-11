from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=600)
        context = browser.new_context()
        page = context.new_page()

        # Step 1: Open Site & Login
        page.goto("https://www.saucedemo.com")
        page.get_by_placeholder("Username").fill("standard_user")
        page.get_by_placeholder("Password").fill("secret_sauce")
        page.get_by_role("button", name="Login").click()

        # Step 2: Product ko Cart mein Add Karna (Role-based locator)
        # Hum pehle item "Sauce Labs Backpack" ka "Add to cart" button click karenge
        page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()

        # Step 3: Cart Icon par jaana aur badge count verify karna
        cart_badge = page.locator(".shopping_cart_badge")
        
        # Web-First Assertion: Auto-wait karke verify karega ke cart count '1' hai ya nahi
        expect(cart_badge).to_have_text("1")
        print("Assertion Passed: Cart Badge Count is 1")

        # Step 4: Cart Open karna
        page.locator(".shopping_cart_link").click()

        # Step 5: Verify item in Cart using Text
        expect(page.get_by_text("Sauce Labs Backpack")).to_be_visible()
        print("Assertion Passed: Item successfully visible in cart!")

        # Step 6: Checkout Process
        page.get_by_role("button", name="Checkout").click()
        
        # Form fill karna
        page.get_by_placeholder("First Name").fill("Shiza")
        page.get_by_placeholder("Last Name").fill("Testing")
        page.get_by_placeholder("Zip/Postal Code").fill("44000")
        page.get_by_role("button", name="Continue").click()
        page.get_by_role("button", name="Finish").click()

        # Step 7: Final Success Message Check
        success_msg = page.get_by_role("heading", name="Thank you for your order!")
        expect(success_msg).to_be_visible()
        print("Complete Order Flow Passed!")

        browser.close()

if __name__ == "__main__":
    run()