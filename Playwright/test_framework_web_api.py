import json
import time
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page
import pytest #importing page class which will provide the fixtre of
from pageObjects.login import LoginPage
from pageObjects.dashboard import DashboardPage #importing the login page class from the page objects folder to use the methods of the login page in the test case. this is used to create a page object model for the login page. so that we can reuse the code for login in multiple test cases. this is a good practice to follow in automation testing.
from utils.api_base_framework import APIUtils
from pytest_bdd import scenarios, given, when, then, parsers

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

    username = user_credentials["userEmail"] #this will extract the user email from the user credentials. this is used to get the username for login.
    password = user_credentials["userPassword"] #this will extract the user password from the user credentials. this is used to get the password for login.

    #login to the application 
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credentials["userEmail"]) #this will fill the email field with the user email from the json file. we are using the user credentials from the json file to fill the login form. this is a good practice to externalize the data from the code and use it in the test. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    page.locator("#userPassword").fill(user_credentials["userPassword"])
    page.locator("#login").click()
    time.sleep(1) #doing this to check the login functionality working with below POM model.


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

@pytest.mark.parametrize('user_credentials', user_credentials_list) #this will run the test for each set of user credentials in the list. this is used to run the test for multiple user credentials.
def test_POM_login(playwright: Playwright, user_credentials): #have to make sure this user_credentials is returning the parameter
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils() #creating an object of the APIUtils class to call the methods inside this method.
    order_id = api_utils.create_order(playwright, user_credentials=user_credentials) #this will create an order using the api and return the order id. we can use this order id to verify the order in the ui. we are passing the user credentials to the create_order method to get the token for that particular user and then create the order for that user. this is a good practice to follow in automation testing. because we can create orders for multiple users and then verify them in the ui.

    #putting the values in the variables to make it more readable.
    username = user_credentials["userEmail"] #this will extract the user email from the user credentials. this is used to get the username for login.
    password = user_credentials["userPassword"] #this will extract the user password from the user credentials. this is used to get the password for login.

    #logging in to the website using the POM model to login from the login file with login class and its methods.

    login_page = LoginPage(page) #creating an object of the LoginPage class to call the constructor and pass the page object to it. this is used to create a page object model for the login page. so that we can reuse the code for login in multiple test cases. this is a good practice to follow in automation testing.
    login_page.navigate_to_login()
    dashboard_page = login_page.login(username, password)
    dashboard_page.select_orders_link() #this will call the method to click on the orders link from the dashboard page. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard in multiple test cases. this is a good practice to follow in automation testing.
    time.sleep(1)
    print("Login successful with user: " + username)

    #order history page
    ordeHistoryPage = dashboard_page.select_orders_link() #this will call the method to click on the orders link from the dashboard page and return the order history page object. this is used to create a page object model for the order history page. so that we can reuse the code for order history page in multiple test cases. this is a good practice to follow in automation testing.
    orderDetails=ordeHistoryPage.select_order(order_id) #this will call the method to select the order from the order history page. this is used to create a page object model for the order history page. so that we can reuse the code for order history page in multiple test cases. this is a good practice to follow in automation testing.
    orderDetails.verifyOrderMessage() #this will call the method to verify the order message from the order details page. this is used to create a page object model for the order details page. so that we can reuse the code for order details page in multiple test cases. this is a good practice to follow in automation testing.
    print("Order details are fetched successfully for order id: " + order_id)
    context.close()
    """#dashborad page object and selecting the orders link
    dashboard_page = DashboardPage(page) #creating an object of the DashboardPage class to call the constructor and pass the page object to it. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard in multiple test cases. this is a good practice to follow in automation testing.
    dashboard_page.select_orders_link() #this will call the method to click on the orders link"""
 
    #instead of the above whole creating a new object, we can call the function directly from login page


    browser.close()

@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_BDD_login(playwright: Playwright, user_credentials): #have to make sure this user_credentials is returning the parameter
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    api_utils = APIUtils() #creating an object of the APIUtils class to call the methods inside this method.
    order_id = api_utils.create_order(playwright, user_credentials=user_credentials) #this will create an order using the api and return the order id. we can use this order id to verify the order in the ui. we are passing the user credentials to the create_order method to get the token for that particular user and then create the order for that user. this is a good practice to follow in automation testing. because we can create orders for multiple users and then verify them in the ui.

    #putting the values in the variables to make it more readable.
    username = user_credentials["userEmail"] #this will extract the user email from the user credentials. this is used to get the username for login.
    password = user_credentials["userPassword"] #this will extract the user password from the user credentials. this is used to get the password for login.

    #logging in to the website using the POM model to login from the login file with login class and its methods.

    login_page = LoginPage(page) #creating an object of the LoginPage class to call the constructor and pass the page object to it. this is used to create a page object model for the login page. so that we can reuse the code for login in multiple test cases. this is a good practice to follow in automation testing.
    login_page.navigate_to_login()
    dashboard_page = login_page.login(username, password)
    dashboard_page.select_orders_link() #this will call the method to click on the orders link from the dashboard page. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard in multiple test cases. this is a good practice to follow in automation testing.
    time.sleep(1)
    print("Login successful with user: " + username)

    #order history page
    ordeHistoryPage = dashboard_page.select_orders_link() #this will call the method to click on the orders link from the dashboard page and return the order history page object. this is used to create a page object model for the order history page. so that we can reuse the code for order history page in multiple test cases. this is a good practice to follow in automation testing.
    orderDetails=ordeHistoryPage.select_order(order_id) #this will call the method to select the order from the order history page. this is used to create a page object model for the order history page. so that we can reuse the code for order history page in multiple test cases. this is a good practice to follow in automation testing.
    orderDetails.verifyOrderMessage() #this will call the method to verify the order message from the order details page. this is used to create a page object model for the order details page. so that we can reuse the code for order details page in multiple test cases. this is a good practice to follow in automation testing.
    print("Order details are fetched successfully for order id: " + order_id)
    context.close()
    """#dashborad page object and selecting the orders link
    dashboard_page = DashboardPage(page) #creating an object of the DashboardPage class to call the constructor and pass the page object to it. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard in multiple test cases. this is a good practice to follow in automation testing.
    dashboard_page.select_orders_link() #this will call the method to click on the orders link"""
 
    #instead of the above whole creating a new object, we can call the function directly from login page


    browser.close()
