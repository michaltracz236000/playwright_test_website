import re
from playwright.sync_api import Page, expect
import time

def test_decline_cookies(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    expect(page.get_by_text("Odrzuć")).to_be_hidden()

def test_choose_tyre_size1(page: Page):
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

def test_choose_tyre_size2(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimWidth").select_option("185")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimRatio").select_option("70")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimDiameter").select_option("15")
    time.sleep(1)
    expect(page.locator("#_carTires_ctTS_ddlDimWidth")).to_have_value("185")
    expect(page.locator("#_carTires_ctTS_ddlDimRatio")).to_have_value("70")
    expect(page.locator("#_carTires_ctTS_ddlDimDiameter")).to_have_value("15")

def test_choose_tyre_size3(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimWidth").select_option("245")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimRatio").select_option("45")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimDiameter").select_option("17")
    time.sleep(1)
    expect(page.locator("#_carTires_ctTS_ddlDimWidth")).to_have_value("245")
    expect(page.locator("#_carTires_ctTS_ddlDimRatio")).to_have_value("45")
    expect(page.locator("#_carTires_ctTS_ddlDimDiameter")).to_have_value("17")

def test_choose_tyre_size4(page: Page):
    page.goto("https://www.oponeo.pl")
    page.locator("#consentsBar > div > div > span.reject.button.primary.md.solid").click()
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimWidth").select_option("275")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimRatio").select_option("65")
    time.sleep(1)
    page.locator("#_carTires_ctTS_ddlDimDiameter").select_option("20")
    time.sleep(1)
    expect(page.locator("#_carTires_ctTS_ddlDimWidth")).to_have_value("275")
    expect(page.locator("#_carTires_ctTS_ddlDimRatio")).to_have_value("65")
    expect(page.locator("#_carTires_ctTS_ddlDimDiameter")).to_have_value("20")
    
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

