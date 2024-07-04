from playwright.sync_api import APIRequestContext


def x_test_get_access_api(api_request_context: APIRequestContext):
    response = api_request_context.get("https://api.github.com/user/repos")
    assert response.status == 200, "Request to /user/repos failed"
