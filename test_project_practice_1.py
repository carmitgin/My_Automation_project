from playwright.sync_api import Page, expect

def test_validate_admin_has_system_options(page: Page):
    '''As an admin i will excpect that after login the system menue will be visible'''
    
    page.goto("https://sv-students-recommend.onrender.com/")
    page.locator("[data-test='input-email']").fill("hagai@svcollege.co.il")
    page.locator("[data-test='input-password']").fill("test1234")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_url("**/pages/home.html")
    expect(page.locator("[data-test='nav-system']")).to_be_visible()    