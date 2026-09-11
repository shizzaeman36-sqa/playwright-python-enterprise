import os
import pytest
from dotenv import load_dotenv
from login_page import LoginPage

# .env file se hidden values load karne ke liye
load_dotenv()

@pytest.fixture
def login_p(page):
    login_obj = LoginPage(page)
    
    # .env file se URL read kar rahe hain
    base_url = os.getenv("BASE_URL")
    page.goto(base_url)
    
    return login_obj