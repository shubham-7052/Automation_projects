from playwright.sync_api import Page
import logging
from playwright.sync_api import expect
import pytest

def test_handle_alerts(page:Page):
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")

    # #Get the element by placeholder and verify it is visible
    page.get_by_placeholder("Hide/Show Example").scroll_into_view_if_needed()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    # #verify the element is hidden after clicking on hide button
    page.get_by_role("button", name= "Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()

    # #Handle the alert and verify the alert text
    page.on("dialog", lambda dialog: dialog.accept())
    page.get_by_role("button", name= "Confirm").click()
   
    with page.expect_popup() as new_page:
        page.click('#openwindow')
    new_page = new_page.value
    print(f"new_page.url: {new_page.url}")
    expect(new_page.get_by_role("link", name = 'Courses').nth(0)).to_be_visible()
    new_page.wait_for_timeout(2000)
    new_page.close()
    

    #Switch into page frame and verify the element is visible
    frame_page = page.frame_locator('#courses-iframe')
    frame_page.get_by_role('link', name='VIEW ALL COURSES').scroll_into_view_if_needed()
    expect(frame_page.get_by_role('link', name='VIEW ALL COURSES')).to_be_visible()
    expect(frame_page.locator("div.sec-title.centered.light h2")).to_contain_text("Our Students")
    page.wait_for_timeout(2000)
