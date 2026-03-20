from playwright.sync_api import Page


def test_window_handle(page:Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    # Get the current page URL and print it
    with page.expect_popup() as new_page:
        page.get_by_text("Free Access to InterviewQues/ResumeAssistance/Material").click()
    new_page = new_page.value
    print(f"new_page.url: {new_page.url}")
    text = new_page.locator(".im-para.red").text_content()
    page.wait_for_timeout(5000)
    print(f"text: {text}")
    new_page.close()
    page.close()