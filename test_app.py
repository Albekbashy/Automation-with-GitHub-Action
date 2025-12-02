from hello_world import app, greet

def test_greet():
    assert greet() == "Welcome to CI/CD 101 using GitHub Actions!"

def test_greeting_route():
    client = app.test_client()
    response = client.get("/greeting")
    assert response.status_code == 200
    assert b"Welcome to CI/CD 101 using GitHub Actions!" in response.data
