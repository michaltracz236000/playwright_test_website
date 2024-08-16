import re
from playwright.sync_api import Page, expect
import time

def test_has_title(page: Page):
    page.goto("https://www.oponeo.pl")
    time.sleep(5)

    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(5)