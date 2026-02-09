import pytest

@pytest.fixture(scope='session')
def user_credentials(request): #this is global request parameter. use this to acces global enviroment.
   return request.param #this will return the parameter which we are passing in the test function. this is used to get the user credentials for login. we are using the user credentials from the json file to fill the login form. this is a good practice to externalize the data from the code and use it in the test. so that we can easily maintain the data and also we can easily change the data without changing the code. this is a good practice to follow in automation testing.