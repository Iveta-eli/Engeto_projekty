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

def test_check_h2(browser):
    browser.goto("https://engeto.cz/")
    h2 = browser.query_selector("h2.wp-block-heading.engeto-narrow#h-neni-cas-ztracet-cas-vyber-si-svuj-kurz-programovani")
    assert h2 is not None
    assert h2.inner_text() == "NENÍ ČAS ZTRÁCET ČAS – VYBER SI SVŮJ KURZ PROGRAMOVÁNÍ"