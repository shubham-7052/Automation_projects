from playwright.sync_api import Playwright

class APIUtils:

    def create_token(self,playwright:Playwright):
        print("Creating token")
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        data_payload = {"userEmail":"shubham.gupta1154@gmail.com","userPassword":"Monotype123#"}
        response = api_request_context.post(url="/api/ecom/auth/login",data=data_payload)
        assert response.ok
        token = response.json()["token"]
        print(f"token: {token}")
        return token

    def create_order(self,playwright:Playwright):
        print("Creating an order")
        api_request_context = playwright.request.new_context(base_url="https://rahulshettyacademy.com")
        data_payload = {"orders":[{"country":"India","productOrderedId":"6960eac0c941646b7a8b3e68"}]}
        token = self.create_token(playwright)
        headers = {"Content-Type":"application/json","Authorization" : token}
        response = api_request_context.post(url= "api/ecom/order/create-order", data=data_payload, headers=headers)
        print(f"response.status: {response.status}")
        print(f"response.json {response.json()}")
        assert response.ok
        return response.json()['orders'][0]