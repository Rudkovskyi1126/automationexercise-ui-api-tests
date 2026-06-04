import pytest

from api.helpers import expect


def test_create_user(created_user, api_client):
    response = api_client.get("/getUserDetailByEmail", params={"email": created_user["email"]})
    body = expect(response, code=200)
    assert body["user"]["email"] == created_user["email"]


def test_update_user(created_user, api_client):
    response = api_client.put("/updateAccount", data={"name": "TesT_1234", "email": created_user["email"], "password": created_user["password"]})
    expect(response, code=200, message="User updated!")


def test_delete_user(user_payload, api_client):
    api_client.post("/createAccount", data=user_payload)
    response = api_client.delete("/deleteAccount", data={"email": user_payload["email"], "password": user_payload["password"]})
    expect(response, code=200, message="Account deleted!")


def test_verify_login_valid_credentials(created_user, api_client):
    response = api_client.post("/verifyLogin", data={"email": created_user["email"], "password": created_user["password"]})
    expect(response, code=200)


def test_verify_login_invalid_credentials(api_client):
    response = api_client.post("/verifyLogin", data={"email": "test_wrong@examle.com", "password": "wrongpassword"})
    expect(response, code=404, message="User not found!")


def test_verify_login_missing_email(api_client):
    response = api_client.post("/verifyLogin", data={"password": "123456789"})
    expect(response, code=400, message="Bad request, email or password parameter is missing in POST request.")


@pytest.mark.parametrize("email", [
    "notanemail",
    "two@@example.com",
    "@example.com",
    "user@",
    "user@nonexistentdomain12345.xyz",
])
def test_verify_login_invalid_email_format(api_client, email):
    response = api_client.post("/verifyLogin", data={"email": email, "password": "password123"})
    assert response.json()["responseCode"] != 200


def test_get_all_products(api_client):
    response = api_client.get("/productsList")
    body = expect(response, code=200)
    assert "products" in body
    assert len(body["products"]) > 0


@pytest.mark.parametrize("keyword", ["top", "dress", "jeans"])
def test_search_products(api_client, keyword):
    response = api_client.post("/searchProduct", data={"search_product": keyword})
    body = expect(response, code=200)
    assert "products" in body
    assert len(body["products"]) > 0


def test_search_product_missing_param(api_client):
    response = api_client.post("/searchProduct")
    expect(response, code=400, message="Bad request, search_product parameter is missing in POST request.")


def test_get_all_brands(api_client):
    response = api_client.get("/brandsList")
    body = expect(response, code=200)
    assert "brands" in body
    assert len(body["brands"]) > 0


@pytest.mark.parametrize("method, endpoint", [
    ("post",   "/productsList"),
    ("put",    "/brandsList"),
    ("delete", "/verifyLogin"),
])
def test_method_not_allowed(api_client, method, endpoint):
    response = getattr(api_client, method)(endpoint)
    expect(response, code=405, message="This request method is not supported.")
