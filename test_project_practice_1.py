from playwright.sync_api import Page, expect
import os
import pytest
from dotenv import load_dotenv

load_dotenv()

BASE = os.getenv("BASE_URL", "https://sv-students-recommend.onrender.com")
ADMIN_USER = os.getenv("ADMIN_USER","")  
PASSWORD = os.getenv("PASSWORD", "") 

def test_validate_admin_has_system_options(page: Page):
    '''As an admin i will excpect that after login the system menue will be visible'''
    
    page.goto(BASE)
    page.locator("[data-test='input-email']").fill(ADMIN_USER)
    page.locator("[data-test='input-password']").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/pages/home.html")
    expect(page.locator("[data-test='nav-system']")).to_be_visible() 

    # Expects page to have a title "system- SV students Reccomend"
    expect(page.get_by_role("heading", name="System management")).to_be_visible()

    
       