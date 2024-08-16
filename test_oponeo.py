import re
from playwright.sync_api import Page, expect
import time

def test_decline_cookies(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(5)
    expect(page.get_by_text("Odrzuć")).to_be_hidden()