from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto('http://localhost/')

    page.locator('input[name="sheetId"]').fill('http://localhost/files/radar.csv')
    page.locator('a.button').click()

    # Wait for "Your Technology Radar will be available in just a few seconds"
    page.wait_for_selector('div#radar')

    page.screenshot(path='artifacts/byor.png', full_page=True)
    page.pdf(path='artifacts/byor.pdf', format='A4')

    browser.close()
