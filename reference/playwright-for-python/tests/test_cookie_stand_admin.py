import pytest

def test_login(page):
    page.goto("https://cookie-stand-admin-reference.vercel.app/")

    assert page.title() == "Cookie Stand Admin"
    assert page.inner_text("button") == "SIGN IN"

    username_value = page.locator("text=USER NAME").input_value()
    password_value = page.locator("text=PASSWORD").input_value()

    assert username_value == ''
    assert password_value == ''


def test_home_page_values(logged_in_page):
    assert logged_in_page.locator("input[name='min']").input_value() == '0'
    assert logged_in_page.locator("input[name='max']").input_value() == '0'
    assert logged_in_page.locator("input[name='avg']").input_value() == '0'
    

def test_home_page_navigation(logged_in_page):
    anchor = logged_in_page.locator("table a").first
    url = anchor.get_attribute("href")

    with logged_in_page.expect_navigation(url=url):
        anchor.click()
    
    
def test_detail_page(logged_in_page):
    anchor = logged_in_page.locator("table a").first
    url = anchor.get_attribute("href")
    stand_name = anchor.text_content()
    anchor.click()
    
    assert logged_in_page.url.endswith(url)
    assert stand_name in logged_in_page.inner_text("main")
    

@pytest.fixture
def logged_in_page(page):
    page.goto("https://cookie-stand-admin-reference.vercel.app/")
    
    page.fill('#username','admin')
    page.fill('#password','admin')
    page.click('text=SIGN IN')

    return page
