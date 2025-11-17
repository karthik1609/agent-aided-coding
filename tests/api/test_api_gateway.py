from fastapi.testclient import TestClient

from api_gateway.main import app


client = TestClient(app)


def test_healthcheck() -> None:
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_eligibility_endpoint() -> None:
    payload = {
        "applicant_name": "Test User",
        "amount": 5000,
        "income": 70000,
        "credit_score": 720,
        "existing_debt": 2000,
    }
    response = client.post("/loans/eligibility", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "approved" in data and "rate" in data
