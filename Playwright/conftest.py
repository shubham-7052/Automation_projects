# import pytest
# from playwright.sync_api import sync_playwright

# @pytest.fixture(scope="session")
# def page():
#     with sync_playwright() as p:
#         context = p.chromium.launch_persistent_context(
#             user_data_dir="user_data",  # folder for session storage
#             headless=False
#         )
#         page = context.new_page()
#         yield page
#         context.close()
