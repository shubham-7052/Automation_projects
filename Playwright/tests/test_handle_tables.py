from playwright.sync_api import Page
import logging
from playwright.sync_api import expect
import pytest

def test_handle_table(page:Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    #Get the table element and print the number of rows and columns
    headers = page.locator("th")
    for i in range(headers.count()):
        text = headers.nth(i).text_content().strip()
        if text == "Price":
            price_index = i
        elif text == "Discount price":
            discounted_price_index = i

    print(f"price_index: {price_index}")
    print(f"discounted_price_index: {discounted_price_index}")
    
    

    potato_ele = page.locator('tr').filter(has_text="Potato")
    potato_price = potato_ele.locator('td').nth(price_index).text_content()
    potato_discounted_price = potato_ele.locator('td').nth(discounted_price_index).text_content()
    print(f"potato_price: {potato_price}")
    print(f"potato_discounted_price: {potato_discounted_price}")
            
