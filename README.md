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
| python-dotenv | Environment config |
| GitHub Actions | CI/CD |

---

## Project Structure

```
automationexercise-ui-api-tests/
├── pages/
│   ├── login_page.py       # Login, logout, signup, delete account
│   ├── main_page.py        # Navigation locators
│   └── register_page.py    # Registration form locators and fill method
├── tests/
│   ├── ui/
│   │   └── test_auth.py    # UI auth tests (login, logout, register)
│   └── api/
│       └── test_users.py   # API tests (users, products, brands)
├── conftest.py             # Fixtures: browser, api client, user data
├── pytest.ini              # pytest configuration
├── requirements.txt
└── .env                    # Environment variables (not in git)
```

---

## Test Coverage

### UI Tests — 5 tests

| Test | Scenario | Type |
|------|----------|------|
| test_login_valid_credentials | Login with correct email and password | Positive |
| test_login_invalid_credentials | Login with wrong credentials | Negative |
| test_logout_valid_credentials | Logout after successful login | Positive |
| test_register_new_user | Register with a unique email | Positive |
| test_register_existing_email | Register with an already used email | Negative |

### API Tests — 9 tests

| Test | Method | Endpoint | Scenario |
|------|--------|----------|----------|
| test_create_user | GET | /getUserDetailByEmail | Create user and verify by email |
| test_verify_login_valid_credentials | POST | /verifyLogin | Login with valid credentials |
| test_verify_login_invalid_credentials | POST | /verifyLogin | Login with wrong credentials |
| test_verify_login_missing_email | POST | /verifyLogin | Missing email parameter |
| test_update_user | PUT | /updateAccount | Update user name |
| test_delete_user | DELETE | /deleteAccount | Delete existing user |
| test_get_all_products | GET | /productsList | Get full products list |
| test_get_all_brands | GET | /brandsList | Get full brands list |
| test_search_products | POST | /searchProduct | Search products by keyword |

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
