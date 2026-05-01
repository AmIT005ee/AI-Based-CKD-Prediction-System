# 🩺 AI-Based Chronic Kidney Disease Prediction System

A web-based application that automatically reads medical lab reports, extracts key values using OCR, predicts the stage of Chronic Kidney Disease (CKD), and generates a professional medical report.

---

## 🚀 Project Overview

Chronic Kidney Disease (CKD) is a serious health condition that requires early detection and monitoring.
In traditional systems, doctors manually analyze lab reports, which can be time-consuming and error-prone.

This project aims to **automate the entire process** using:

* OCR (Optical Character Recognition)
* Rule-based prediction logic
* PDF report generation
* Patient data storage

---

## 🎯 Features

* 📄 Upload lab report images
* 🔍 Automatic text extraction using OCR
* 🧠 CKD stage prediction based on lab values
* 📊 Generates structured PDF medical reports
* 🗂️ Stores patient history in database
* ✍️ Manual input option for lab values

---

## ⚙️ Tech Stack

### 🌐 Frontend

* HTML
* CSS

### ⚙️ Backend

* Python
* Flask

### 👁️ OCR & Image Processing

* Tesseract OCR
* OpenCV

### 🧾 Report Generation

* ReportLab

### 🗄️ Database

* SQLite

### 🤖 Machine Learning (Experimental)

* Random Forest
* Firefly Algorithm
* Cuckoo Search

---

## 🧩 System Workflow

1. Upload lab report image or enter values manually
2. Image is processed using OpenCV
3. Text is extracted using Tesseract OCR
4. Important medical values are parsed
5. CKD stage is predicted using creatinine levels
6. PDF report is generated
7. Patient data is stored in database

---

## 🧠 CKD Prediction Logic

| Creatinine Level | CKD Stage |
| ---------------- | --------- |
| ≤ 1.2            | Stage 1   |
| ≤ 1.8            | Stage 2   |
| ≤ 3.0            | Stage 3   |
| ≤ 5.0            | Stage 4   |
| > 5.0            | Stage 5   |

---

## 📁 Project Structure

```
├── app.py              # Main Flask application
├── app2.py             # PDF generation logic
├── templates/
│   └── index.html      # UI page
├── static/
│   └── style.css       # Styling
├── reports/            # Generated PDF reports
├── ckd.csv             # Dataset for ML experiments
├── day1_ckd.ipynb      # Data analysis notebook
├── random_forest.py    # ML model
├── firefly.py          # Feature selection
├── cukoo.py            # Optimization algorithm
└── ckd_db.db           # SQLite database
```

---

## ▶️ How to Run the Project

### 🔹 1. Clone Repository

```
git clone https://github.com/your-username/AI-Based-CKD-Prediction-System.git
cd AI-Based-CKD-Prediction-System
```

---

### 🔹 2. Install Dependencies

```
pip install flask opencv-python pytesseract reportlab pandas numpy scikit-learn
```

---

### 🔹 3. Run the Application

```
python app.py
```

---

### 🔹 4. Open in Browser

```
http://127.0.0.1:5000
```

---

## 📊 Benefits

* ⏱️ Faster CKD screening
* ❌ Reduces manual errors
* 📄 Automated report generation
* 🗂️ Maintains patient history
* 🧠 Easy to extend with ML models

---

## 🔮 Future Improvements

* Integrate real ML-based prediction models
* Improve OCR accuracy for multiple formats
* Add user authentication system
* Use cloud database (MySQL / MongoDB)
* Support PDF uploads and more medical parameters

---

## 📌 Conclusion

This project demonstrates how AI, OCR, and web technologies can be combined to build a practical healthcare solution that improves efficiency, accuracy, and accessibility in disease prediction.

---

## 👨‍💻 Contributors

* Amit Jangle
---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
