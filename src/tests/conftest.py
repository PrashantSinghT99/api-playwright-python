# from playwright.sync_api import Playwright
# from dotenv import load_dotenv
# import pytest
# import os
# import re
# load_dotenv()

# CLIENT_ID = os.getenv("CLIENT_ID")
# assert CLIENT_ID, "CLIENT_ID is not set"

# CLIENT_SECRET = os.getenv("CLIENT_SECRET")
# assert CLIENT_SECRET, "CLIENT_SECRET is not set"

# BASE_URL = os.getenv("BASE_URL")
# assert BASE_URL, "BASE_URL is not set"

# CLIENT_CODE = os.getenv("CLIENT_CODE")
# assert CLIENT_CODE, "CLIENT_CODE is not set"

# @pytest.fixture(scope="session")
# def api_request_context(playwright: Playwright):
#         params = {
#             "client_id": CLIENT_ID,
#             "client_secret": CLIENT_SECRET,
#             "code": CLIENT_CODE
#         }

#         # Step 3: Create a new API request context for authenticated requests
#         api_request_context = playwright.request.new_context(
#             base_url=BASE_URL,
#         )

#         # Step 4: Send a POST request to obtain the access token
#         response = api_request_context.get(
#             "/login/oauth/access_token", params=params)
        
#         assert response.status == 200, f"Failed to get access token: {response.status}"
#         # Extract the access token from the response
#         response_text = response.text()
#         pattern = r'access_token=([^&]*)'
#         match = re.search(pattern, response_text)

#         if match:
#             token = match.group(1)
#             auth_context = playwright.request.new_context(
#             base_url=BASE_URL,
#             extra_http_headers={"Authorization": f"Bearer {token}"}
#         )
#         else:
#             print("Access token not found")
#             raise ValueError("Access token not found in the response")
     
#         # Update the API request context with the obtained access token
#         # api_request_context.set_extra_http_headers({"Authorization": f"Bearer {access_token}"})

#         yield auth_context

#         # Cleanup: Dispose of the API request context after the session ends
#         auth_context.dispose()



# DUMMY APIS TESTING
import pytest
from playwright.sync_api import Playwright
from dotenv import load_dotenv
import os
load_dotenv()


BASE_URL=os.getenv("BASE_URL")
assert BASE_URL,"BASE_URL not set"


@pytest.fixture(scope="session")
def set_api_context(playwright:Playwright):
    
    api_context=playwright.request.new_context(
        base_url=BASE_URL
    )
    
    yield api_context
    
    api_context.dispose()

