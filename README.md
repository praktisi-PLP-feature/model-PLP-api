# PERSONALIZED LEARNING PATH - PROJECT - FASTAPI 
##### Submission akhir dari dicoding dengan salah satu dataset yaitu **Bike Sharing**, pada project ini diberlakukan analisis rental sepeda dan deployment menggunakan dashboard Streamlit, ada beberapa hal yang dilakukan dalam analisis seperti memahami data untuk menumbuhkan pertanyaan permasalahan, eksplorasi data, hingga visualisasi data untuk memenuhi pertanyaan yang telah ditentukan. Akses project pada link berikut : 

> link github_repo : https://github.com/anazantoro/dicoding-project-analisis-data <br>
link colab_notebook : https://colab.research.google.com/drive/1iA_MlL4dHzPCdtOY8J_eaKohD-7K23yH?usp=sharing

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
