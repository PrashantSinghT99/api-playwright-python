from playwright.sync_api import APIRequestContext


def test_post_a_product(set_api_context: APIRequestContext, shared_data):
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        "title": 'BMW',
    }
    response = set_api_context.post("/products/add", headers=header, data=data)
    # print(response.json())
    shared_data['id'] = response.json()['id']
    assert response.status == 201, "Product cannot be created/added"
    assert response.json()['title'] == "BMW", "Product title assertion failed"


