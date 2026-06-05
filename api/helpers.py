
def expect(response, *, status=200, code=None, message=None, reason=None):
    prefix = f"[{reason}] " if reason else ""
    assert response.status_code == status, \
        f"{prefix}Expected status {status}, got {response.status_code}"
    body = response.json()
    if code is not None:
        assert body["responseCode"] == code, \
            f"{prefix}Expected responseCode {code}, got {body.get('responseCode')}"
    if message is not None:
        assert body["message"] == message, \
            f"{prefix}Expected message '{message}', got '{body.get('message')}'"
    return body
