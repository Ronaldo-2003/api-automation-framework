def assert_status_code(response, expected_status):
    assert response.status_code == expected_status, (
        f"Expected status {expected_status}, "
        f"but got {response.status_code}"
    )


def assert_json_has_keys(response_json, expected_keys):
    for key in expected_keys:
        assert key in response_json, f"Missing key: {key}"
