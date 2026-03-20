from playwright.sync_api import Playwright
from playwright.sync_api import expect
from tests.utils.test_api_base import APIUtils


class TestE2ETesting:

    def test_e2e_testing(self,playwright:Playwright):
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://rahulshettyacademy.com/client")
        page.get_by_placeholder('email@example.com').fill("shubham.gupta1154@gmail.com")
        page.get_by_placeholder('enter your passsword').fill('Monotype123#')
        page.get_by_role('button',name='Login').click()

        page.get_by_role('button',name='ORDERS').click()
        api_utils = APIUtils()
        order_id = api_utils.create_order(playwright)
        print(f"order_id: {order_id}")
        page.get
        page.wait_for_timeout(5000)
        page.reload()
        page.wait_for_timeout(5000)
        row_order = page.locator('tr').filter(has_text=order_id)
        row_order.get_by_role('button', name= 'View').click()
        page.wait_for_timeout(5000)
        expect(page.locator('.email-preheader')).to_have_text("Thank you for Shopping With Us")
        expect(page.locator('.col-text.-main')).to_have_text(order_id)
        page.wait_for_timeout(5000)
        page.close()
        browser.close()


