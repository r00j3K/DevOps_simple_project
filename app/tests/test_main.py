import socket
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200

    data = response.json()

    assert "hostname" in data
    assert "version" in data

    assert data["version"] == "1.0.0"

    host_val = f"Hostname: {socket.gethostbyname()}"

    assert data["hostname"] == host_val
