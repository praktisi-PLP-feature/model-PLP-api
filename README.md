# PERSONALIZED LEARNING PATH - PROJECT - FASTAPI 
##### API ini digunakan untuk memprediksi kategori bidang teknologi informasi yang paling relevan bagi seorang mahasiswa berdasarkan skor minat atau kemampuan. Model machine learning yang digunakan memberikan rekomendasi bidang beserta materi pembelajarannya.

🛠️ Tech Stack
FastAPI
TensorFlow / Keras
Pydantic
fastAPI
Uvicorn 
Pytest 

📂 Project Structure
```
plp-api/
├── requirements.txt
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── data/
│   │   └── materials.py
│   ├── model/
│   │   ├── model_loader.py
│   │   ├── model.h5
│   │   └── scaler.pkl
│   ├── schemas/
│   │   └── prediction.py
│   ├── service/
│   │   └── predictor.py
│   └── tests/
│       └── test_api.py
```

## Clone Project
  Clone file project dari repository ini gunakan git clone
  ```
  git clone https://github.com/praktisi-PLP-feature/model-PLP-api
  ```

## Setup Unittest
Tetap di Root Project
```
PYTHONPATH=. pytest tests/
```

## Setup FastAPI - Bash
1. Buat virtual environment
  ```
  python -m venv venv
  ```
2. Aktivasi virtual environment
  ```
  source venv/Scripts/activate
  ```
3. Install library sesuai dengan apa yang ada di **requirements.txt**
  ```
  pip install -r requirements.txt
  ```
4. Run FastAPI
   Tetap di Root Project
  ```
  fastapi dev app/main.py
  ```
  Server akan berjalan di:
  http://127.0.0.1:8000/docs

📤 API Usage
Endpoint: /predict , Method: POST

Request Body (JSON):
```
{
    "uiux": 40,
    "programming": 50,
    "operational": 20,
    "datascience": 30,
    "cybersec": 80,
    "qa": 70,
    "network": 70
}
```

Response (Example):
```
{
    "status": "success",
    "threshold": 0.50,
    "predictions": [
        {
            "category": "Cybersecurity",
            "probability": 0.99,
            "material": {
                "title": "Step by step guide to becoming a Cyber Security",
                "urls": [
                    "https://roadmap.sh/cyber-security"
                ]
            }
        }
    ]
}
```
