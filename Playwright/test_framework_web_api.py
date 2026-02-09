import json
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page
import pytest #importing page class which will provide the fixtre of
from utils.api_base import APIUtils

with open('data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials_list = test_data["user_credentials"] #this will extract the list of user credentials from the json file. this is used to get the user credentials for login.


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_parameter_login(playwright: Playwright, user_credentials): #have to make sure this user_credentials is returning the parameter
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials["userEmail"]) #this will fill the email field with the user email from the json file. we are using the user credentials from the json file to fill the login form. this is a good practice to externalize the data from the code and use it in the test. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    page.locator("#userPassword").fill(user_credentials["userPassword"])
    page.locator("#login").click()
    time.sleep(1)
      

@pytest.mark.parametrize('user_credentials', user_credentials_list) #this will run the test for each set of user credentials in the list. this is used to run the test for multiple user credentials.
def test_e2e_web_api(playwright: Playwright, user_credentials): #have to make sure this user_credentials is returning the parameter
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    #create order from API
    api_utils = APIUtils() #creating an object of the APIUtils class to call the methods inside this method.
    order_id = api_utils.create_order(playwright) #this will create an order using the api and return the order id. we can use this order id to verify the order in the ui.

    #login to the application
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials["userEmail"]) #this will fill the email field with the user email from the json file. we are using the user credentials from the json file to fill the login form. this is a good practice to externalize the data from the code and use it in the test. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    page.locator("#userPassword").fill(user_credentials["userPassword"])
    page.locator("#login").click()
    time.sleep(1)

    #checking the order history
    page.get_by_role("button", name="Orders").click()
    time.sleep(5)
    row_coat_order_id = page.locator("tr").filter(has_text=order_id)
    row_coat_order_id.get_by_role("button", name="View").click() #this will scan only that particular row which has the order id and then click on the view button. this is very useful when we have multiple orders in the order history and we want to verify only a particular order. so we can use this approach to scan only that particular row which has the order id and then click on the view button.
    time.sleep(5)
    #page.screenshot(path=screenshot_path + "screenshot/orderconfirmation.png")
    expect(page.locator(".tagline")).to_have_text("Thank you for Shopping With Us")
    
    browser.close()

#json file to extract the details. Externalizing the data from the code is a good practice. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
