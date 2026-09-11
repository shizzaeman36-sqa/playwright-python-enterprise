from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        context = browser.new_context()
        page = context.new_page()

        # ==========================================
        # SCENARIO 1: FILE UPLOAD
        # ==========================================
        page.goto("https://the-internet.herokuapp.com/upload")

        # Set input files direct input field par file path attach karta hai
        # Hum pehle se bani state.json file ko hi dummy upload ke liye use kar rahe hain
        page.locator("#file-upload").set_input_files("state.json")
        page.get_by_role("button", name="Upload").click()

        # Verify karte hain ke file upload hui ya nahi
        uploaded_file_text = page.locator("#uploaded-files").text_content()
        print("Uploaded File Name:", uploaded_file_text.strip())


        # ==========================================
        # SCENARIO 2: FILE DOWNLOAD
        # ==========================================
        page.goto("https://the-internet.herokuapp.com/download")

        # Download event ko expect karne ke liye context manager use karte hain
        with page.expect_download() as download_info:
            # First file download link par click kar rahe hain
            page.locator("div.example a").first.click()

        download = download_info.value

        # Downloaded file ko apne custom name aur path se save kar rahe hain
        download_path = download.path()
        saved_path = "downloaded_sample_file.txt"
        download.save_as(saved_path)

        print("File Downloaded & Saved Successfully at:", saved_path)

        browser.close()

if __name__ == "__main__":
    run()