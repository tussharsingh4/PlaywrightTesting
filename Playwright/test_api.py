from playwright.sync_api import Playwright

def test_api_get(playwright: Playwright):
    request = playwright.request.new_context()
    response = request.get('https://jsonplaceholder.typicode.com/posts/1')
    assert response.status == 200
    print(response.json())
 