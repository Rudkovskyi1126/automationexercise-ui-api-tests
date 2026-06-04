

def expect(response, *, status=200, code=None, message=None):
    assert response.status_code == status
    body = response.json()
    if code is not None:
        assert body["responseCode"] == code
    if message is not None:
        assert body["message"] == message
    return body
