import json
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page
import pytest #importing page class which will provide the fixtre of
from pageObjects.dashboard import DashboardPage
from pageObjects.login import LoginPage

with open('data/credentials.json') as f:
        test_data = json.load(f)
        print(test_data)
        user_credentials_list = test_data["user_credentials"] #this will extract the list of user credentials from the json file. this is used to get the user credentials for login.


@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_login_with_POM(playwright: Playwright, user_credentials):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    username = user_credentials["userEmail"] #this will extract the user email from the user credentials. this is used to get the username for login.
    password = user_credentials["userPassword"] #this will extract the user password from the user credentials. this is used to get the password for login.

    login_page = LoginPage(page) #creating an object of the LoginPage class to call the
    login_page.navigate_to_login()
    login_page.login(username, password)
    time.sleep(1)

    #dashborad page object and selecting the orders link
    """orders_page = DashboardPage(page) #creating an object of the DashboardPage class to call the
    orders_page.select_orders_link()
    time.sleep(1)
    browser.close()"""
    #instead of the above whole creating a new object, we can call the function directly from login page
    dashboard_page = login_page.login(username, password) #this will return the dashboard page object to the test case so that we can use the methods of the dashboard page in the test case. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard page in multiple test cases. this is a good practice to follow in automation testing.

    #dashboard page
    dashboard_page.select_orders_link()

