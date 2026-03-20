from playwright.sync_api import Page
from playwright.sync_api import expect


def test_login_example(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label('Username:').fill("rahulshettyacademy")
    page.get_by_label('Password:').fill("Learning@830$3mK2")
    # page.get_by_role('radio', name='User').check()
    # page.get_by_label('User').nth(1).check()
    page.get_by_role('combobox').select_option('Teacher')
    page.get_by_role('checkbox', name='terms').check()
    page.wait_for_timeout(2000)
    page.get_by_role('button', name='Sign In').click()
    page.wait_for_timeout(2000)
    page.locator('app-card').filter(has_text='Samsung Note 8').get_by_role('button', name='Add').click()
    page.wait_for_timeout(2000)
    page.locator('app-card').filter(has_text='iphone X').get_by_role('button', name='Add').click()
    page.wait_for_timeout(2000)
    page.get_by_text('Checkout').click()
    page.wait_for_timeout(2000)
    count = page.locator('.media-body').count()
    list = []
    for i in range(0, count):
        card = page.locator('.media-body').nth(i)
        text = card.locator('h4 a').inner_text()
        list.append(text)
    print(f"count: {list}")
