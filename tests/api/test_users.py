import pytest


def test_create_user(created_user, api_client):
    response = api_client.get("/getUserDetailByEmail", params={"email": created_user["email"]})
    data = response.json()
    assert response.status_code == 200
    assert data["user"]["email"] == created_user["email"]


def test_update_user(created_user, api_client):
    response = api_client.put("/updateAccount", data={"name": "TesT_1234", "email": created_user["email"], "password": created_user["password"]})
    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "User updated!"


def test_delete_user(user_payload, api_client):
    api_client.post("/createAccount", data=user_payload)
    response = api_client.delete("/deleteAccount", data={"email": user_payload["email"], "password": user_payload["password"]})
    data = response.json()
    assert data["responseCode"] == 200
    assert data["message"] == "Account deleted!"


def test_verify_login_valid_credentials(created_user, api_client):
    response = api_client.post("/verifyLogin", data={"email": created_user["email"], "password": created_user["password"]})
    data = response.json()
    assert response.status_code == 200
    assert data["responseCode"] == 200


def test_verify_login_invalid_credentials(api_client):
    response = api_client.post("/verifyLogin", data={"email": "test_wrong@examle.com", "password": "wrongpassword"})
    data = response.json()
    assert data["responseCode"] == 404
    assert data["message"] == "User not found!"


def test_verify_login_missing_email(api_client):
    response = api_client.post("/verifyLogin", data={"password": "123456789"})
    data = response.json()
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, email or password parameter is missing in POST request."


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
    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0


@pytest.mark.parametrize("keyword", ["top", "dress", "jeans"])
def test_search_products(api_client, keyword):
    response = api_client.post("/searchProduct", data={"search_product": keyword})
    data = response.json()
    assert data["responseCode"] == 200
    assert "products" in data
    assert len(data["products"]) > 0


def test_search_product_missing_param(api_client):
    response = api_client.post("/searchProduct")
    data = response.json()
    assert data["responseCode"] == 400
    assert data["message"] == "Bad request, search_product parameter is missing in POST request."


def test_get_all_brands(api_client):
    response = api_client.get("/brandsList")
    data = response.json()
    assert data["responseCode"] == 200
    assert "brands" in data
    assert len(data["brands"]) > 0


@pytest.mark.parametrize("method, endpoint", [
    ("post",   "/productsList"),
    ("put",    "/brandsList"),
    ("delete", "/verifyLogin"),
])
def test_method_not_allowed(api_client, method, endpoint):
    response = getattr(api_client, method)(endpoint)
    data = response.json()
    assert data["responseCode"] == 405
    assert data["message"] == "This request method is not supported."
