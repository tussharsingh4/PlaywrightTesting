import pytest
from playwright.sync_api import Playwright, expect

@pytest.fixture(scope='session')
def user_credentials(request): #this is global request parameter. use this to acces global enviroment.
   return request.param #this will return the parameter which we are passing in the test function. this is used to get the user credentials for login. we are using the user credentials from the json file to fill the login form. this is a good practice to externalize the data from the code and use it in the test. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.

@pytest.fixture(scope='session')
def browser_instance(playwright: Playwright, request):
   browser = playwright.chromium.launch(headless=False) 
   context = browser.new_context()
   page = context.new_page()
   yield page #this will setup and teardown the browser in this session itself.
   context.close()
   browser.close()
   #fixturs get executed till the yield, and then go to the function which is calling this fixture and then after the function execution is completed, it will come back to the fixture and execute the code after the yield. this is a good way to setup and teardown the browser in the same session.