import pytest
from playwright.sync_api import APIRequestContext
 
def test_put_a_product(set_api_context: APIRequestContext):
    # product_id = shared_data.get('id')
    header = {
        'Content-Type': 'application/json'
    }
    data = {
        "title": 'Mercedes',
    }
    # response = set_api_context.put(f"/products/{product_id}", headers=header, data=data)
    response = set_api_context.put(f"/products/1", headers=header, data=data)
    print(response.json())
    assert response.status == 200, "Product cannot be created/added"
    assert response.json()[
        'title'] == "Mercedes", "Product title assertion failed"
