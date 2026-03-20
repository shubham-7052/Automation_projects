from playwright.sync_api import Playwright
from playwright.sync_api import Page
from playwright.sync_api import expect

respone = {"data":[],"message":"No Orders"}
def intercept_response(route):
    print("intercept_response_event_handler called")
    route.fulfill(json = respone)

def intercept_request(route):
    print("intercept_request_event_handler called")
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=699725321fe6115f6a958d3d")


def test_network_intercepting_response(page:Page):
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')
    # intercept the network request and mock the response
    page.route("https://rahulshettyacademy.com/api/ecom/user/get-cart-products/*", intercept_response)
    page.get_by_placeholder('email@example.com').fill("shubham.gupta1154@gmail.com")
    page.get_by_placeholder('enter your passsword').fill('Monotype123#')
    
    page.get_by_role('button',name='Login').click()
    for i in range(0, 2):
        page.get_by_role('button', name='Add To Cart').nth(i).click()
    page.wait_for_timeout(5000)
    page.locator(".btn.btn-custom").filter(has_text="Cart").click()
    page.wait_for_timeout(5000)
    expect(page.locator(".ng-star-inserted")).to_have_text("No Products in Your Cart !")
    page.wait_for_timeout(5000)
    page.close()

def test_network_intercepting_request(page:Page):
    page.goto('https://rahulshettyacademy.com/client/#/auth/login')
    # intercept the network request and mock the request url
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.get_by_placeholder('email@example.com').fill("shubham.gupta1154@gmail.com")
    page.get_by_placeholder('enter your passsword').fill('Monotype123#')
    
    page.get_by_role('button',name='Login').click()
    for i in range(0, 2):
        page.get_by_role('button', name='Add To Cart').nth(i).click()
    page.wait_for_timeout(5000)
    page.get_by_role('button', name= 'ORDERS').click()
    page.wait_for_timeout(5000)
    page.get_by_role('button', name= 'View').first.click()
    page.wait_for_timeout(5000)
    expect(page.get_by_text("You are not authorize to view this order")).to_be_visible()
    page.wait_for_timeout(5000)
    page.close()

def test_inject_session_cookie(playwright:Playwright):
    app_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2OTkzMzZmMDFmZTYxMTVmNmE4YWM3MWMiLCJ1c2VyRW1haWwiOiJzaHViaGFtLmd1cHRhMTE1NEBnbWFpbC5jb20iLCJ1c2VyTW9iaWxlIjo3MDUyNzk3OTA3LCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzcxNTIxNTMyLCJleHAiOjE4MDMwNzkxMzJ9.0IFeuWRnZZ9VOhkRPGlKY3xxwTrbT3mNnMhX9z7IKZw"
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    # Inject the token into local storage before navigating to the page
    page.add_init_script(f"""localStorage.setItem('token','{app_token}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.wait_for_timeout(5000)
    expect(page.get_by_text("Automation Practice")).to_be_visible()
    page.wait_for_timeout(5000)
    page.close()
    browser.close()
        
