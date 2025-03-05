import pytest
from fastapi.testclient import TestClient

from app import app

client = TestClient(app)

@pytest.fixture
def clear_tasks():
    app.tasks = []

def test_add_task(clear_tasks):
    response = client.post("/add?task=LearnCI_CD")
    assert response.status_code == 200
    assert response.json() == {"message":"LearnCI_CD"}

# def test_read_tasks(clear_tasks):
#     client.post("/add?task=LearnCI_CD")
#     response = client.get("/")
#     assert response.status_code == 200
#     data = response.json()
#     assert "tasks" in data
#     assert data["tasks"] == ["LearnCI_CD"]
