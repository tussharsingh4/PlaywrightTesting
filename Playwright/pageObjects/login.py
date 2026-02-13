from pageObjects.dashboard import DashboardPage #imported the package from which after login, I will be loading the dashboard page.


class LoginPage:

    def __init__(self, page): #this is a contructor with self parameter as default. this will initialize the page object and also the locators for the username, password and login button. this is used to create a page object model for the login page. so that we can reuse the code for login in multiple test cases. this is a good practice to follow in automation testing.
        self.page = page #local class reference to the page object which is passed as a parameter in the constructor

    def navigate_to_login(self):
        self.page.goto("https://rahulshettyacademy.com/client") #this will navigate to the login page. we can use this method in the test cases to navigate to the login page before performing any actions on the login page.
    
    def login(self, username, password):
        self.page.locator("#userEmail").fill(username) #this will fill the email field with the username passed as a parameter in the login method. this is used to perform the login action on the login page. we can use this method in the test cases to perform the login action on the login page.
        self.page.locator("#userPassword").fill(password) #this will fill the password field with the password passed as a parameter in the login method. this is used to perform the login action on the login page. we can use this method in the test cases to perform the login action on the login page.
        self.page.locator("#login").click() #this will click on the login button. this is used to perform the login action on the login page. we can use this method in the test cases to perform the login action on the login page.
        
        dashboard_page = DashboardPage(self.page) #creating an object of the DashboardPage class to call the select_orders_link method. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard page in multiple test cases. this is a good practice to follow in automation testing.
        return dashboard_page #returning the dashboard page object to the test case so that we can use the methods of the dashboard page in the test case. this is used to create a page object model for the dashboard page. so that we can reuse the code for dashboard page in multiple test cases. this is a good practice to follow in automation testing.
        #here, once logged in, I will see the dashboard page, so instead of creating a new object everytime, I can create object here and catch in the main test.

        #This should always be done when you know that after performing the login on this page, this will always navigate to the new dashboard page.