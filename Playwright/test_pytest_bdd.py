import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from playwright.sync_api import Playwright, expect

from pageObjects.login import LoginPage
from utils.api_base_framework import APIUtils


scenarios('Feature/Login.feature')

@pytest.fixture
def shared_data():
    return {} #this is sharing an empty dictionary. once declared as fixture, can be used anywhere in the test. this is used to share data between different step definition files. this is a good practice to share data between different step definition files. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.


@given(parsers.parse('Place item order with {username} and {password}')) #to cath it in bdd, here in step definition file we use curly braces to specify the parameter which we are passing from the feature file. this is used to parameterize the test and make it more flexible. so that we can run the same test with different data without changing the code. this is a good practice to follow in automation testing.
def place_item_order(playwright: Playwright, username, password, shared_data):

    user_credentials = {}                           #this is a dictionary which will store the user credentials. we can use this dictionary to pass the user credentials to the api call. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    
    user_credentials["userEmail"] = username        #this will store the username in the dictionary with the key as userEmail. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    user_credentials["userPassword"] = password     #this will store the password in the dictionary with the key as userPassword. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.

    api_utils = APIUtils()                          #creating an object of the APIUtils class to call the methods inside this method.
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data["order_id"] = order_id              #returning the order id to the next step definition file to use it in the next step definition file. this is a good practice to return the data from one step definition file to another step definition file. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.


@given('the user is on landing page')
def user_on_landing_page(browser_instance, shared_data): #can access fixture as an argument in python.
    login_page = LoginPage(browser_instance) #creating an object of the LoginPage class to call the methods inside this method. this is used to create a page object model for the login page. so that we can reuse the code for login in multiple test cases. this is a good practice to follow in automation testing.
    login_page.navigate_to_login()
    shared_data["login_page"] = login_page #storing the login page object in the shared data dictionary with the key as login_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.

@when(parsers.parse('I login to portal with {username} and {password}'))
def user_login_with_valid_credentials(username, password, shared_data):
    login_page = shared_data["login_page"]                  #getting the login page object from the shared data dictionary with the key as login_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    dashboard_page = login_page.login(username, password)   #this will call the login method of the login page and pass the username and password as parameters to perform the login action on the login page. this is used to perform the login action on the login page. we can use this method in the test cases to perform the login action on the login page.
    shared_data["dashboard_page"] = dashboard_page          #storing the dashboard page object in the shared data dictionary with the key as dashboard_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.

    
@when('I navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data["dashboard_page"]          #getting the dashboard page object from the shared data dictionary with the key as dashboard_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    order_page = dashboard_page.select_orders_link()                      #this will call the select_orders_link method of the dashboard page to navigate to the orders page. this is used to perform the action of navigating to the orders page from the dashboard page. we can use this method in the test cases to perform the action of navigating to the orders page from the dashboard page.
    shared_data["order_page"] = order_page              #storing the order page object in the shared data dictionary with the key as order_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.


@when('select the orderId')
def select_order_id(shared_data):
    orderHistoryPage = shared_data["order_page"]          #getting the order page object from the shared data dictionary with the key as order_page. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    order_id = shared_data["order_id"]                    #getting the order id from the shared data dictionary with the key as order_id. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    orderDetailsPage =orderHistoryPage.select_order(order_id)            #this will call the select_order_id
    shared_data["orderDetails_Page"] = orderDetailsPage    #storing the order details page object in the shared data dictionary with the key as orderDetailsPage. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.



@then('I should see the order details with order success message')
def order_message_should_be_displayed(shared_data):
    orderDetailsPage = shared_data["orderDetails_Page"]    #getting the order details page object from the shared data dictionary with the key as orderDetailsPage. this is a good practice to store the data in a dictionary and then use it in the code. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.
    orderDetailsPage.verifyOrderMessage()                 #this will call the verify_order_success_message method of the order details page to verify the order success message. this is used to perform the action of verifying the order success message on the order details page. we can use this method in the test cases to perform the action of verifying the order success message on the order details page.