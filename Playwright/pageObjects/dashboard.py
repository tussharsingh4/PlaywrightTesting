from pageObjects.orders import OrdersPage


class DashboardPage:
    def __init__(self, page):
        self.page = page
    
    def select_orders_link(self):
        self.page.get_by_role("button", name="Orders").click()
        orderHistoryPage = OrdersPage(self.page) #creating an object of the OrdersPage class to call the
        return orderHistoryPage #returning the order history page object to the test case so that we can use the methods of the order history page in the test case. this is used to create a page object model for the order history page. so that we can reuse the code for order history page in multiple test cases. this is a good practice to follow in automation testing.

#we know that after clicking the orders link, I will land on the orders page so I initiated it from the dashboard page itself. this is a good practice to follow in automation testing. because we know that after performing the action on this page, it will always navigate to the new page. so we can create the object of the new page in the current page and return it to the test case. this way we can reuse the code for the new page in multiple test cases without creating the object of the new page in each test case. this is a good practice to follow in automation testing.