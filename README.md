# 🏦 End-to-End Credit Risk Scoring System

[![Hugging Face Spaces](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Spaces-blue)](https://huggingface.co/spaces/rizukaf/credit-score)
[![Python 3.12](https://img.shields.io/badge/Python-3.12-yellow)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Enabled-blue)](https://www.docker.com/)

**Live Demo:** [Klik Disini untuk Mencoba Aplikasi](https://huggingface.co/spaces/rizukaf/credit-score)

## 📋 Project Overview
Project ini bertujuan untuk memprediksi probabilitas gagal bayar (*default risk*) calon nasabah menggunakan **Machine Learning**. Sistem ini dirancang untuk membantu analis kredit membuat keputusan yang lebih cepat dan berbasis data.

Tantangan utama dalam dataset ini adalah *Imbalanced Data* (jumlah nasabah macet jauh lebih sedikit dibanding nasabah lancar), yang diatasi menggunakan teknik **Gradient Boosting** dan **Threshold Adjustment**.

---

## 🧠 Business Logic: The 5C Framework
Dalam memilih fitur (variabel) untuk model, saya tidak sembarangan memasukkan semua kolom. Saya menggunakan pendekatan perbankan standar **5C of Credit** untuk memastikan model menilai risiko dari segala sisi:

### 1. Character (Karakter & Reputasi)
Menilai kemauan nasabah untuk membayar utang berdasarkan riwayat masa lalu.
* **Fitur:** `EXT_SOURCE_2`
* **Penjelasan:** Skor normalisasi dari data eksternal (seperti BI Checking/SLIK). Ini adalah indikator terkuat perilaku nasabah sebelumnya.

### 2. Capacity (Kemampuan Bayar)
Menilai apakah gaji nasabah cukup untuk membayar cicilan tanpa mengganggu kebutuhan hidup.
* **Fitur:** `AMT_INCOME_TOTAL`, `AMT_ANNUITY`
* **Feature Engineering:**
    * **Debt-to-Income Ratio (DIR):** (`AMT_ANNUITY` / `AMT_INCOME_TOTAL`). Mengukur persentase gaji yang habis untuk cicilan.

### 3. Capital (Modal/Aset Pribadi)
Menilai posisi keuangan nasabah secara umum.
* **Fitur:** `FLAG_OWN_CAR`, `FLAG_OWN_REALTY`
* **Penjelasan:** Kepemilikan rumah atau mobil menandakan stabilitas finansial dan bisa menjadi "bantalan" jika terjadi krisis ekonomi pada nasabah.

### 4. Collateral (Jaminan/Tujuan Kredit)
Menilai nilai barang yang dibiayai dibandingkan dengan jumlah pinjaman.
* **Fitur:** `AMT_GOODS_PRICE`, `AMT_CREDIT`
* **Feature Engineering:**
    * **Loan-to-Value (LTV):** (`AMT_CREDIT` / `AMT_GOODS_PRICE`). Jika rasionya > 1.0, artinya nasabah meminjam lebih besar dari harga barang (berisiko *over-leverage*).

### 5. Condition (Kondisi Eksternal/Demografi)
Faktor latar belakang yang bisa memengaruhi risiko.
* **Fitur:** `NAME_EDUCATION_TYPE`, `NAME_INCOME_TYPE`, `REGION_RATING_CLIENT`, `AGE` (Derived from days birth).
* **Penjelasan:** Jenis pekerjaan dan tingkat pendidikan seringkaliberkorelasi dengan stabilitas pendapatan jangka panjang.

---

## 🛠️ Technical Architecture
Project ini dibangun dengan konsep **Full-Stack Data Science**:

1.  **Machine Learning Pipeline:**
    * Preprocessing: Imputation (Median for skewed data), StandardScaler, OneHotEncoder.
    * Model: **Gradient Boosting Classifier**.
    * Evaluation Metric: **ROC-AUC** (0.71) - Dipilih karena lebih fair daripada Akurasi untuk data tidak seimbang.
2.  **Backend (API):**
    * Dibangun menggunakan **FastAPI**.
    * Melakukan kalkulasi ulang fitur turunan (*Feature Engineering*) secara real-time saat user input data.
3.  **Frontend (UI):**
    * Dibangun menggunakan **Streamlit** untuk kemudahan interaksi user.
4.  **Deployment:**
    * Containerization menggunakan **Docker**.
    * Hosted di **Hugging Face Spaces**.

---

## 🚀 How to Run Locally

### Menggunakan Docker (Recommended)
Pastikan Docker Desktop sudah terinstall.

```bash
# 1. Clone Repository
git clone [https://github.com/rizukaf/credit-scoring-app.git](https://github.com/rizukaf/credit-scoring-app.git)
cd credit-scoring-app

# 2. Build Image
docker build -t credit-app .

# 3. Run Container
docker run -p 7860:7860 -p 8000:8000 credit-app
```
Akses aplikasi di browser: http://localhost:7860
📊 Model Performance

    Training ROC-AUC: 0.76

    Validation ROC-AUC: 0.71

    Insight: Model memiliki performa yang stabil (tidak overfitting parah) dan mampu membedakan nasabah berisiko dengan probabilitas 71%.

Created by Rizka F. as part of Data Science Portfolio.
