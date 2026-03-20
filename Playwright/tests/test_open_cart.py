from playwright.sync_api import Page
import logging
from playwright.sync_api import expect
import pytest

class TestOpenCart:

    def test_checkout_cart(self, page:Page):
        page.goto("https://www.opencart.com/")
        title = page.title()
        print(f"title: {title}")

        # Click the header Login link (scoped to avoid duplicate matches)
        header_login = page.locator('.navbar-right.hidden-xs').get_by_role('link', name='Login')
        header_login.click()

        # Wait for the login page to load and assert the visible H1
        page.wait_for_timeout(10000)
        page.screenshot(path="opencart_login.png")
        expect(page.locator('h1')).to_have_text("Log in to your OpenCart account")
        page.wait_for_timeout(2000)