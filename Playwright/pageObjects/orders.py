from pageObjects.orderDetails import OrderDetails


class OrdersPage:
    def __init__(self, page):
        self.page = page
        
    def select_order(self, order_id): #this method is to select the order from the order history page. this is used to select the order from the order history page. we can use this method in the test cases to select the order from the order history page.
        row = self.page.locator("tr").filter(has_text=order_id) #this will scan only that particular row which has the order id. this is very useful when we have multiple orders in the order history and we want to verify only a particular order. so we can use this approach to scan only that particular row which has the order id and then click on the view button.
        row.get_by_role("button", name="View").click() #this will click on the view button of that particular row which has the order id. this is used to select the order from the order history page. we can use this method in the test cases to select the order from the order history page.
        orderDetailsPage = OrderDetails(self.page) #creating an object of the orderDetailsPage class to call the method to verify the order message. this is used to create a page object model for the order details page. so that we can reuse the code for order details page in multiple test cases. this is a good practice to follow in automation testing.
        return orderDetailsPage #returning the order details page object to the test case so that we can use the methods of the order details page in the test case. this is used to create a page object model for the order details page. so that we can reuse the code for order details page in multiple test cases. this is a good practice to follow in automation testing.
    