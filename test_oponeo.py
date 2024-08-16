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
    
def test_choose_tyre_type1(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupPremium > div.groupTitle > label > span > span").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_olProducers_lbAck0").click()
    expect(page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div > div.dropdown > span")).to_have_text("9 wybranych")

def test_choose_tyre_type2(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupMedium > div.groupTitle > label > span > span").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_olProducers_lbAck0").click()
    expect(page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div > div.dropdown > span")).to_have_text("12 wybranych")


def test_choose_tyre_type3(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div").click()
    time.sleep(1)
    page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer.visible > div > div.options > div > div.producersGroup > div.groupItem.groupCheap > div.groupTitle > label > span > span").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_olProducers_lbAck0").click()
    expect(page.locator("#forSize > div:nth-child(2) > div.chooseBox.producer > div > div.dropdown > span")).to_have_text("84 wybranych")

