# 🏦 End-to-End Credit Risk Scoring

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/rizukaf/credit-score)

**Live Demo:** [Klik di sini untuk mencoba aplikasi](https://huggingface.co/spaces/rizukaf/credit-score)

## 🎯 Business Overview
Lembaga keuangan perlu memprediksi kemampuan bayar nasabah secara akurat untuk mengurangi NPL (Non-Performing Loan). Proyek ini menggunakan pendekatan **5C of Credit** untuk memfilter fitur yang relevan.

## 🛠 Tech Stack
* **Model:** Random Forest & Gradient Boosting (Scikit-Learn).
* **Preprocessing:** Scikit-Learn Pipeline (Imputation, Scaling, Encoding).
* **Backend:** FastAPI (Microservice Architecture).
* **Frontend:** Streamlit.
* **Deployment:** Docker & Render.

## 📊 Model Performance
* **ROC-AUC Score:** 0.71 (Validation Set).
* **Handling Imbalance:** Menggunakan Class Weight Adjustment & Gradient Boosting.

## 🚀 How to Run Locally (Docker)
1. Clone repository ini.
2. Pastikan Docker Desktop menyala.
3. Jalankan perintah:
```bash
docker build -t credit-app .
docker run -p 8501:8501 -p 8000:8000 credit-app
```
4. Buka browser di `http://localhost:8501`.

---
*Created by Rizka Fiddiyansyah as part of Portfolio Project.*

