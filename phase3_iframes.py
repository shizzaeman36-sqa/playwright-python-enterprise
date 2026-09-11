from playwright.sync_api import sync_playwright, expect

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=800)
        context = browser.new_context()
        page = context.new_page()

        # iFrame wali practice site par jaate hain
        page.goto("https://the-internet.herokuapp.com/iframe")

        # Step 1: iFrame ko locate karte hain (frame_locator se)
        # Is page par editor iFrame id "#mce_0_ifr" ke andar hai
        editor_frame = page.frame_locator("#mce_0_ifr")

        # Step 2: iFrame ke andar jo body tag hai, usko select karke content interact karte hain
        # Pehle se maujood text clear karke apna text type karte hain
        editor_body = editor_frame.locator("#tinymce")
        
        editor_body.clear()
        editor_body.fill("Hello Shiza! We are automating inside an iFrame successfully!")

        # Step 3: Verify karte hain ke text iFrame mein fill ho gaya
        expect(editor_body).to_have_text("Hello Shiza! We are automating inside an iFrame successfully!")
        print("iFrame Automation Passed!")

        browser.close()

if __name__ == "__main__":
    run()