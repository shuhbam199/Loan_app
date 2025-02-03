from app import app
import json
import pytest

@pytest.fixture
def client():
    return app.test_client()

def test_home(client):
    resp = client.get("/")
    assert resp.status_code == 200

def test_aboutus(client):
    resp = client.get("/aboutus")
    assert resp.status_code == 200
    assert b"WE ARE MLOPS2" in resp.data

def test_predict(client):
    test_data = {'Gender': "Male", 'Married': "Unmarried", 'ApplicantIncome': 50000, 'Credit_History': "Cleared Debts", 'LoanAmount': 500000}
    resp = client.post("/prediction", json=test_data)
    assert resp.status_code == 200
    assert resp.json =={'loan_approval_status': 'Rejected'}