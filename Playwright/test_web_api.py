import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page #importing page class which will provide the fixtre of

from utils.api_base import APIUtils

def test_e2e_web_api(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order from API
    api_utils = APIUtils() #creating an object of the APIUtils class to call the methods inside this method.
    order_id = api_utils.create_order(playwright) #this will create an order using the api and return the order id. we can use this order id to verify the order in the ui.

    #login to the application
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    time.sleep(1)

    #checking the order history
    page.get_by_role("button", name="Orders").click()
    time.sleep(5)
    row_coat_order_id = page.locator("tr").filter(has_text=order_id)
    row_coat_order_id.get_by_role("button", name="View").click() #this will scan only that particular row which has the order id and then click on the view button. this is very useful when we have multiple orders in the order history and we want to verify only a particular order. so we can use this approach to scan only that particular row which has the order id and then click on the view button.
    time.sleep(5)
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")

    browser.close()