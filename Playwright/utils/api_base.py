
from playwright.sync_api import Playwright

order_paylaod = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"},{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"},{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}
class APIUtils: #this utility is going to create an order using the calls to the api.

    def get_token(self, playwright:Playwright):
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com") #this is to set the base url for all the api calls. so that we dont have to write the full url every time.
        response = api_request_context.post("/api/ecom/auth/login", data={"userEmail":"rahulshetty@gmail.com","userPassword":"Iamking@000"}) #these details are stored as dictionary above. Key value pair.
        #this will return true if the response status code is 200. this is a method which will check the status code of the response. if it is 200, then it will return true. otherwise, it will return false.
        print(response.json())
        response_body = response.json() #this will convert the response into json format. so that we can easily read it and use it for further processing.
        token = response.json()["token"] #this will extract the token from the response. this is a method which will convert the response into json format. so that we can easily read it and use it for further processing.
        return token #this will return the token to the caller. so that we can use it for further processing. like we can use it to create order or we can use it to delete the order from the api.

    def create_order(self, playwright:Playwright): #even when doing api or ui automation.

        token = self.get_token(playwright) #we have to get the token first before creating the order. because we need the token for authentication. so we can call the get_token method here to get the token and then use it for creating the order.
        
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com") #this is to set the base url for all the api calls. so that we dont have to write the full url every time.
        
        response = api_request_context.post("/api/ecom/order/create-order", data=order_paylaod,  headers={"Content-Type":"application/json", "Authorization": token}) #these details are stored as dictionary above. Key value pair.
        #here we are sending a post request to the api with endpoin, headers and data. at this website, we will hit a create-order api request.
        #sending headers is very important for authentication.
        
        print(response.json()) #this will print the response in json format. this is a method which will convert the response into json format. so that we can easily read it and use it for further processing.
        response_body = response.json() #this will convert the response into json format. so that we can easily read it and use it for further processing.
        #response_body["orders"] #this is giving a list of orders which we have created. because we are sending a list of orders in the request payload. so it is giving a list of orders in the response as well.
        #to extract the first order id, writing the code below
        order_id = response_body["orders"][0] #this will extract the first order id from the response. because we are sending a list of orders in the request payload. so it is giving a list of orders in the response as well. so we can extract the first order id from the list of orders in the response.
        print(order_id) #this will print the order id which we have extracted from the response
        return order_id #this will return the order id to the caller. so that we can use it for further processing. like we can use it to verify the order in the ui or we can use it to delete the order from the api.