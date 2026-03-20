from playwright.sync_api import Page
import logging
class TestBookFlight:


    def test_book_flight(self,page:Page):
        page.goto("https://blazedemo.com/")
        page.locator("select").first.select_option("Boston")
        page.wait_for_timeout(2000)
        # page.get_by_role("combobox").nth(0).select_option("Paris")
        # page.wait_for_timeout(2000)
        # page.select_option("//select[@name='fromPort']",value="Boston")
        # page.wait_for_timeout(2000)
        # page.select_option("//select[@name='fromPort']", label="Portland")
        # page.wait_for_timeout(2000)
        # page.select_option("//select[@name='fromPort']", index=2)
        # page.wait_for_timeout(2000)
        selected_value = page.locator("select[name='fromPort']").input_value()
        logging.info(f"selected_value : {selected_value}")
        print(selected_value)
        page.select_option("select[name='toPort']", label='London' )
        page.wait_for_timeout(2000)
        # page.select_option("select[name='toPort']", index=2)
        # page.wait_for_timeout(2000)
        # page.select_option("select[name='toPort']", value='Berlin')
        # page.wait_for_timeout(2000)
        # page.get_by_role('combobox').nth(1).select_option('Dublin')
        
        page.click('input[value="Find Flights"]')
        # page.get_by_role('button', name='Find Flights').click()
        page.wait_for_timeout(2000)

        page.locator("tr", has_text="Virgin America").get_by_role("button", name="Choose This Flight").first.click()

        page.wait_for_timeout(2000)

        page.get_by_label("Name").nth(0).fill("Shubham Gupta")
        page.get_by_label("Address").fill("123 Main St")
        page.get_by_label("City").fill("New York")
        page.get_by_label("State").fill("NY")
        page.get_by_label("Zip Code").fill("10001")
        # Not working because of label issue in the application
        # page.get_by_label("Card Type").select_option(value="amex") 
        # page.get_by_role("combobox", name="Card Type").select_option(label="American Express")
        page.select_option('#cardType', value="amex")
        page.get_by_label("Credit Card Number").fill("1234567890123456")
        page.get_by_label("Month").fill("12")
        page.get_by_label("Year").fill("2025")
        page.get_by_label("Name on Card").fill("Shubham Gupta")
        page.get_by_role("button", name = 'Purchase Flight').click()
        page.wait_for_timeout(2000)

        assert "Thank you for your purchase today!" in page
        page.wait_for_timeout(52000)
        page.screenshot(path="blazedemo_booking.png")
        page.close()
        page.wait_for_timeout(5000)


