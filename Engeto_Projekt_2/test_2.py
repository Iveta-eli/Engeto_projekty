import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context()
        page = context.new_page()
        yield page
        browser.close()

def test_check_button(browser):
    browser.goto("https://engeto.cz/")
    browser.evaluate("document.querySelector('#cookiescript_injected_wrapper')?.remove()")
    button = browser.query_selector("a.block-button.type-premium.size-l.orange-link.hide-mobile")
    assert button is not None
    assert button.get_attribute("href") == "/terminy/"
    assert button.is_visible()
    button.click()
    assert browser.url.endswith("/terminy/")
