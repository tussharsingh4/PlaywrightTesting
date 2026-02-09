from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import Page #importing page class which will provide the fixtre of page in testbasic
import time

from Playwright.utils.api_base import APIUtils

fakePayloadResponse = {"data":[],"message":"No Orders"} #when all orders are deleted, this is the response we will get from the api call.
#1 make apic call from browse -> api call contact srver return back response->browser use response to generate html-> display to user
def intercept_route(route): #trying to get all information from the api call
    route.fulfill(
        json = fakePayloadResponse
    ) #this will fullfill the request and give the response back to the page. this is used to intercept the request and give a custom response back to the page.

def test_network(playwright: Playwright) -> None: #this arrow sign is used to specify the return type of the function. in this case, it is None because this function does not return anything. it is just a test function which will perform some actions and then close the browser.
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_route) # * this will consider it as regex and accept any value in place of star.
    page.locator("#userEmail").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    time.sleep(1)
    page.get_by_role("button", name="Orders").click() #once this event is executed, the api call will be intercepted and the custom response will be given back to the page and then the page will be rendered accordingly.
    order_text = page.locator(".mt-4" ).text_content() #this will get the text content of the element which has the class mt-4. this is used to verify the response we are getting from the api call.
    print(order_text) #printing the order text to the console. this is used to verify the response we are getting from the api call.
    assert order_text == "You have No Orders to show at this time. Please Visit Back Us" #this will verify that the order text



def intercept_request(route): #trying to get all information from the api call
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=6984ba88c941646b7ad79e99") #this will continue the request and give the response back to the page. this is used to intercept the request and give a custom response back to the page. this is used when we want to modify the request before it is sent to the server. for example, we can add some headers or we can change the request payload before it is sent to the server. in this case, we are just continuing the request without modifying it.
    #intercept the request and continue the call with new url.

def test_network2(playwright: Playwright): #this function is to intercept request calls. We will sent order id and ask for more details and in this case we will send order id of another person's account.
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request) # * this will consider it as regex and accept any value in place of star. this will intercept the requst
    page.locator("#userEmail").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.locator("#login").click()
    page.get_by_role("button", name="Orders").click()
    page.get_by_role("button", name="View").first.click() #this will click the first element which has the role button and name view. this is used to click the view button of the first order in the order history. once this button is clicked, the api call will be intercepted and the custom response will be given back to the page and then the page will be rendered accordingly.
    message = page.locator(".blink-me").text_content() #this will get the text content of the element which has the class mt-4. this is used to verify the response we are getting from the api call.
    print(message) #printing the message text to the console. this is used to verify the response we are getting from the api call.

def test_session_storage(playwright: Playwright): #bypass login and go to orders page directly by setting session storage.
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    api_utils = APIUtils() #creating an object of the APIUtils class to call the methods inside this method.
    get_token = api_utils.get_token(playwright) #this will get the token from the api call and return it. we can use this token to set the session storage and then we can bypass the login and go to the orders page directly.
    #scrip to inject token into session storage
    page.add_init_script(f"""localStorage.setItem("token", "{get_token}");""") #this will add the token to the session storage before the page is loaded. this is used to bypass the login and go to the orders page directly.
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="Orders").click() #once this event is executed, the api call will be intercepted and the custom response will be given back to the page and then the page will be rendered accordingly.
    expect(page.get_by_text("Your Orders"))