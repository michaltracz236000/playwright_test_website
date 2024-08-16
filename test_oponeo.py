import re
from playwright.sync_api import Page, expect
import time

def test_decline_cookies(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    expect(page.get_by_text("Odrzuć")).to_be_hidden()

def test_choose_tyre_size(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimWidth").select_option("215")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimRatio").select_option("55")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimDiameter").select_option("17")
    time.sleep(1)
    expect(page.locator("#_carTires_ctTS_ddlDimWidth")).to_have_value("215")
    expect(page.locator("#_carTires_ctTS_ddlDimRatio")).to_have_value("55")
    expect(page.locator("#_carTires_ctTS_ddlDimDiameter")).to_have_value("17")
    
