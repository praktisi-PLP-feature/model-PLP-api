from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_valid_prediction():
    """
    Memastikan API menghasilkan prediksi yang benar saat input sesuai ekspektasi.
    """
    response = client.post("/predict", json={
        "scores": [0.5, 0.7, 0.4, 0.6, 0.5, 0.7, 0.4]
    })
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "success"
    assert "threshold" in data
    assert "predictions" in data
    assert isinstance(data["predictions"], list)
    assert len(data["predictions"]) == 3  


def test_invalid_input_length():
    """
    Menguji bagaimana API menangani input tidak valid dengan panjang data yang salah.
    """
    response = client.post("/predict", json={
        "scores": [0.5, 0.7]  # Salah panjang
    })
    assert response.status_code in [400, 422]


def test_invalid_data_type():
    """
    Memastikan API menolak input dengan tipe data tidak sesuai.
    """
    response = client.post("/predict", json={
        "scores": ["wrong", "data", "type", "should", "be", "float", 0.4]
    })
    assert response.status_code == 422
