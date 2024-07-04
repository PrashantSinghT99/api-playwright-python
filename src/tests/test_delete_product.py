from playwright.sync_api import APIRequestContext


def test_delete_a_product(set_api_context:APIRequestContext):
    response=set_api_context.delete('/products/1')
    response_data=response.json()['title']
    response_delete=response.json()["isDeleted"]
    assert response.status == 200,"Request to fetch all products failed"
    assert response_data == "Essence Mascara Lash Princess","Title for product 1 not matching"
    assert response_delete == True,"isDelete not true"