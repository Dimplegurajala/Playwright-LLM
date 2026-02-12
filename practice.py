from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False,slow_mo=2000)
    page= browser.new_page()
    page.goto('https://www.celcomsolutions.com//', wait_until ='networkidle')
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    element = page.get_by_role("img", name= "test-automation", exact= False)
    element.wait_for(state='attached',timeout=10000)
    element.scroll_into_view_if_needed()
    element.click()
    actual_title= page.title()
    expected_title = "Streamline BSS Testing with Test Automation"

    assert actual_title== expected_title, f"The title mismatch: {actual_title}"

    browser.close()
    
