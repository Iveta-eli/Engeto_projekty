# Iveta Eliášková

from playwright.sync_api import sync_playwright

def test_open_page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)  # Změněno na headless=True
        page = browser.new_page()
        page.goto("https://engeto.cz/")
        assert page.title() == "Kurzy programování a dalších IT technologií | ENGETO"
        browser.close()

if __name__ == "__main__":
    test_open_page()