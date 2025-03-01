# tests/test_api.py
from fastapi.testclient import TestClient
from src.api.main import app

client = TestClient(app)

def test_get_patch():
    # This test assumes that a patch with id "Patch_001" exists in the test database.
    response = client.get("/patches/Patch_001")
    assert response.status_code == 200

def test_get_vulnerability():
    # This test assumes that a vulnerability with id "CVE-2023-XXXX" exists in the test database.
    response = client.get("/vulnerabilities/CVE-2023-XXXX")
    assert response.status_code == 200
