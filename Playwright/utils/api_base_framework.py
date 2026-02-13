from playwright.sync_api import Playwright

order_paylaod = {"orders":[{"country":"India","productOrderedId":"6960ea76c941646b7a8b3dd5"},{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"},{"country":"India","productOrderedId":"6960eae1c941646b7a8b3ed3"}]}



class APIUtils:

    def get_token(self, playwright: Playwright, user_credentials):
        user_email = user_credentials['userEmail']
        user_Password = user_credentials['userPassword']
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/auth/login",
                                            data={"userEmail": user_email, "userPassword": user_Password})
        
        print(response.json())
        responseBody = response.json()
        return responseBody["token"]

    def create_order(self, playwright: Playwright, user_credentials):
        token = self.get_token(playwright, user_credentials)
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        response = api_request_context.post("/api/ecom/order/create-order",
                                            data=order_paylaod,
                                            headers={"Authorization": token,
                                                     "Content-Type": "application/json"
                                                     })
        print(response.json())
        response_body = response.json()
        orderId = response_body["orders"][1]
        return orderId
