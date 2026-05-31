# automationexercise-ui-api-tests

[![CI](https://github.com/Rudkovskyi1126/automationexercise-ui-api-tests/actions/workflows/ci.yml/badge.svg)](https://github.com/Rudkovskyi1126/automationexercise-ui-api-tests/actions/workflows/ci.yml)

Automated UI and API test suite for [automationexercise.com](https://automationexercise.com), built with Python, Playwright, and pytest.

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3.11 | Language |
| Playwright (sync) | UI automation |
| pytest | Test framework |
| requests | API testing |
| Allure | Test reports |
| python-dotenv | Environment config |
| GitHub Actions | CI/CD |

---

## Project Structure

```
automationexercise-ui-api-tests/
├── pages/
│   ├── login_page.py       # Login, logout, signup, delete account
│   ├── main_page.py        # Navigation and subscription locators
│   ├── register_page.py    # Registration form
│   ├── contact_page.py     # Contact Us form
│   ├── products_page.py    # Product list, search, categories, brands
│   ├── cart_page.py        # Cart actions
│   ├── checkout_page.py    # Checkout flow
│   └── payment_page.py     # Payment form
├── tests/
│   ├── ui/
│   │   ├── test_auth.py        # TC-01 to TC-05
│   │   ├── test_contact.py     # TC-06
│   │   ├── test_test_cases.py  # TC-07
│   │   ├── test_products.py    # TC-08, TC-09, TC-18, TC-19
│   │   ├── test_subscription.py # TC-10, TC-11
│   │   ├── test_cart.py        # TC-12, TC-13, TC-17
│   │   └── test_checkout.py    # TC-14, TC-15, TC-16
│   └── api/
│       └── test_users.py       # 21 API tests
├── conftest.py             # Fixtures: browser, api client, user data
├── pytest.ini              # pytest configuration
├── requirements.txt
└── .env                    # Environment variables (not in git)
```

---

## Test Coverage

### UI Tests — 21 tests

| Test | TC | Scenario |
|------|----|----------|
| test_register_new_user | TC-01 | Register with a unique email |
| test_login_valid_credentials | TC-02 | Login with correct credentials |
| test_login_invalid_credentials | TC-03 | Login with wrong credentials |
| test_logout_valid_credentials | TC-04 | Logout after successful login |
| test_register_existing_email | TC-05 | Register with an already used email |
| test_contact_us_form | TC-06 | Submit Contact Us form |
| test_navigate_to_test_cases_page | TC-07 | Navigate to Test Cases page |
| test_test_cases_content_visible | TC-07 | Verify test cases content is visible |
| test_all_products_page | TC-08 | Verify All Products page |
| test_product_detail_page | TC-08 | Verify product detail page |
| test_search_product | TC-09 | Search for a product by keyword |
| test_subscription_on_home_page | TC-10 | Subscribe via home page footer |
| test_subscription_on_cart_page | TC-11 | Subscribe via cart page footer |
| test_add_products_to_cart | TC-12 | Add multiple products to cart |
| test_product_quantity_in_cart | TC-13 | Verify product quantity in cart |
| test_place_order_register_while_checkout | TC-14 | Place order: register during checkout |
| test_place_order_register_before_checkout | TC-15 | Place order: register before checkout |
| test_place_order_login_before_checkout | TC-16 | Place order: login before checkout |
| test_remove_product_from_cart | TC-17 | Remove product from cart |
| test_view_category_products | TC-18 | View products by category |
| test_view_brand_products | TC-19 | View and cart products by brand |

### API Tests — 21 tests

| Test | Method | Endpoint | Notes |
|------|--------|----------|-------|
| test_create_user_standalone | POST | /createAccount | Create and delete user |
| test_create_user | GET | /getUserDetailByEmail | Verify user exists after creation |
| test_update_user | PUT | /updateAccount | Update user name |
| test_delete_user | DELETE | /deleteAccount | Delete existing user |
| test_verify_login_valid_credentials | POST | /verifyLogin | Login with valid credentials |
| test_verify_login_invalid_credentials | POST | /verifyLogin | Login with wrong credentials |
| test_verify_login_missing_email | POST | /verifyLogin | Missing email parameter |
| test_verify_login_invalid_email_format | POST | /verifyLogin | 5 invalid email formats (parametrized) |
| test_get_all_products | GET | /productsList | Get full products list |
| test_search_products | POST | /searchProduct | 3 keywords: top, dress, jeans (parametrized) |
| test_search_product_missing_param | POST | /searchProduct | Missing search parameter |
| test_get_all_brands | GET | /brandsList | Get full brands list |
| test_method_not_allowed | — | multiple | 3 method/endpoint combos → 405 (parametrized) |

---

## Setup

```bash
# Clone the repo
git clone https://github.com/Rudkovskyi1126/automationexercise-ui-api-tests.git
cd automationexercise-ui-api-tests

# Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
playwright install chromium
```

Create a `.env` file in the project root:

```
BASE_URL=https://automationexercise.com
API_URL=https://automationexercise.com/api
```

---

## Run Tests

```bash
# All tests
pytest

# API tests only
pytest tests/api/ -v

# UI tests only
pytest tests/ui/ -v
```

---

## CI/CD

Tests run automatically via **GitHub Actions** on every push to `main`.
API and UI tests run as separate parallel jobs on `ubuntu-latest`.