from playwright.sync_api import Page, sync_playwright # to enable autosuggestion of metthods in Page class


#Launch chromium broswer
def test_chromium_browser_launch(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")
    assert "Google" in page.title()
    browser.close()

#Launch firefox browser
def test_firefox_browser_launch(playwright):
    firefixBrowser = playwright.firefox.launch(headless=False)
    page = firefixBrowser.new_page()
    page.goto("https://google.com")
    assert "Google" in page.title()
    page.wait_for_timeout(5000)  # 3000 ms = 3 seconds
    firefixBrowser.close()

# chrominum headless mode : single context, single page
def test_playwright_another_example(page:Page):
    page.goto("https://enterprise.monotype.com/")
    assert "Monotype" in page.title()
    page.click('[data-qa-id="home-page-login"]')
    assert "Monotype" in page.title()

    page.get_by_label("Email address").fill("mem.prodsite+shubham@gmail.com")
    page.click('button[value="default"]')
    page.fill('#password', "Monotype123#")
    # page.get_by_label("password-label").click()
    # ele.click()
    # page.get_by_label("Password").fill("Monotype123#")
    page.click('button[value="default"]')
    page.click('md-typography[@tabindex="-1" and text()="DIV Apollo"]')
    page.wait_for_timeout(10000)  # 3000 ms = 3 seconds

def test_get_users():
    with sync_playwright() as p:
        request_context = p.request.new_context()
        response = request_context.get("")



