from playwright.sync_api import Playwright, APIRequestContext

def test_get_access_api(api_request_context: APIRequestContext): 
    response = api_request_context.get("https://api.github.com/user/repos")
    assert response.status == 200, "Request to /user/repos failed"
