
from playwright.sync_api import APIRequestContext

def test_get_all_products(set_api_context:APIRequestContext):
    response=set_api_context.get('/products')
    assert response.status == 200,"Request to fetch all products failed"

def test_get_a_product(set_api_context:APIRequestContext):
    response=set_api_context.get('/products/1')
    response_data=response.json()['title']
    assert response.status == 200,"Request to fetch all products failed"
    assert response_data == "Essence Mascara Lash Princess","Title for product 1 not matching"