def test_get_activities(client):
    # Arrange: `client` fixture provides TestClient and state is default

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert "Chess Club" in data
    assert isinstance(data["Chess Club"]["participants"], list)


def test_signup_success(client):
    # Arrange
    email = "testuser@example.com"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert "Signed up" in response.json().get("message", "")

    # Verify participant was added
    get_resp = client.get("/activities")
    assert email in get_resp.json()["Chess Club"]["participants"]


def test_signup_activity_not_found(client):
    # Arrange
    email = "nobody@example.com"

    # Act
    response = client.post(f"/activities/Nope/signup?email={email}")

    # Assert
    assert response.status_code == 404


def test_signup_already_enrolled(client):
    # Arrange: michael@mergington.edu is pre-enrolled in Chess Club
    email = "michael@mergington.edu"

    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")

    # Assert
    assert response.status_code == 400
