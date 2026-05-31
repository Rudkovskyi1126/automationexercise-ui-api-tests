import pytest
import requests


def test_create_user_standalone(api_url, user_payload):
    post_response = requests.post(f"{api_url}/createAccount", data=user_payload)
    assert post_response.json()["responseCode"] == 201
    assert post_response.json()["message"] == "User created!"
    delete_response = requests.delete(f"{api_url}/deleteAccount", data={"email": user_payload["email"], "password": user_payload["password"]})
    assert delete_response.json()["responseCode"] == 200


def test_create_user(created_user, api_url):
    get_response = requests.get(f"{api_url}/getUserDetailByEmail", params={"email": created_user["email"]})
    assert get_response.status_code == 200
    assert get_response.json()["user"]["email"] == created_user["email"]


def test_update_user(created_user, api_url):
    put_response = requests.put(f"{api_url}/updateAccount", data={"name": "TesT_1234", "email": created_user["email"], "password": created_user["password"]})
    assert put_response.json()["responseCode"] == 200
    assert put_response.json()["message"] == "User updated!"


def test_delete_user(user_payload, api_url):
    requests.post(f"{api_url}/createAccount", data=user_payload)
    delete_response = requests.delete(f"{api_url}/deleteAccount", data={"email": user_payload["email"], "password": user_payload["password"]})
    assert delete_response.json()["responseCode"] == 200
    assert delete_response.json()["message"] == "Account deleted!"


def test_verify_login_valid_credentials(created_user, api_url):
    post_response = requests.post(f"{api_url}/verifyLogin", data={"email": created_user["email"], "password": created_user["password"]})
    assert post_response.status_code == 200
    assert post_response.json()["responseCode"] == 200


def test_verify_login_invalid_credentials(api_url):
    post_response = requests.post(f"{api_url}/verifyLogin", data={"email": "test_wrong@examle.com", "password": "wrongpassword"})
    assert post_response.json()["responseCode"] == 404
    assert post_response.json()["message"] == "User not found!"


def test_verify_login_missing_email(api_url):
    post_response = requests.post(f"{api_url}/verifyLogin", data={"password": "123456789"})
    assert post_response.json()["responseCode"] == 400
    assert post_response.json()["message"] == "Bad request, email or password parameter is missing in POST request."


@pytest.mark.parametrize("email", [
    "notanemail",
    "two@@example.com",
    "@example.com",
    "user@",
    "user@nonexistentdomain12345.xyz",
])
def test_verify_login_invalid_email_format(api_url, email):
    post_response = requests.post(f"{api_url}/verifyLogin", data={"email": email, "password": "password123"})
    assert post_response.json()["responseCode"] != 200


def test_get_all_products(api_url):
    get_response = requests.get(f"{api_url}/productsList")
    assert get_response.json()["responseCode"] == 200
    assert "products" in get_response.json()
    assert len(get_response.json()["products"]) > 0


@pytest.mark.parametrize("keyword", ["top", "dress", "jeans"])
def test_search_products(api_url, keyword):
    post_response = requests.post(f"{api_url}/searchProduct", data={"search_product": keyword})
    assert post_response.json()["responseCode"] == 200
    assert "products" in post_response.json()
    assert len(post_response.json()["products"]) > 0


def test_search_product_missing_param(api_url):
    post_response = requests.post(f"{api_url}/searchProduct")
    assert post_response.json()["responseCode"] == 400
    assert post_response.json()["message"] == "Bad request, search_product parameter is missing in POST request."


def test_get_all_brands(api_url):
    get_response = requests.get(f"{api_url}/brandsList")
    assert get_response.json()["responseCode"] == 200
    assert "brands" in get_response.json()
    assert len(get_response.json()["brands"]) > 0


@pytest.mark.parametrize("method, endpoint", [
    ("post",   "/productsList"),
    ("put",    "/brandsList"),
    ("delete", "/verifyLogin"),
])
def test_method_not_allowed(api_url, method, endpoint):
    response = getattr(requests, method)(f"{api_url}{endpoint}")
    assert response.json()["responseCode"] == 405
    assert response.json()["message"] == "This request method is not supported."