# 🎗️ Breast Cancer Prediction Using Machine Learning

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-orange?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-learn">
  <img src="https://img.shields.io/badge/Pandas-Data%20Processing-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/Tailwind%20CSS-UI-06B6D4?style=for-the-badge&logo=tailwindcss&logoColor=white" alt="Tailwind CSS">
</p>

<p align="center">
  <b>A Machine Learning-powered web application for breast tumor classification using a Random Forest Classifier.</b>
</p>

<p align="center">
  Built with ❤️ using Python, Flask, Scikit-learn and Tailwind CSS.
</p>

---

## 📌 1. Project Overview

**Breast Cancer Prediction Using Machine Learning** is a web-based machine learning application that predicts whether a breast tumor is likely to be **Benign** or **Malignant** based on selected tumor measurements.

The application uses a **Random Forest Classifier** trained on breast cancer diagnostic data and provides an easy-to-use web interface where users can enter tumor-related features and receive a model prediction.

### 🎯 Project Objective

The main objective of this project is to demonstrate how machine learning can be integrated into a real-world web application to perform binary classification.

### 🔄 Prediction Flow

```text
User Input
    ↓
Flask Web Application
    ↓
Input Data Processing
    ↓
Random Forest Classifier
    ↓
Prediction
    ↓
Confidence Score
    ↓
Result Display
```

---

## ✨ 2. Features

* 🎗️ Breast tumor classification
* 🤖 Random Forest machine learning model
* 🌐 Flask-based web application
* 🎨 Responsive Tailwind CSS interface
* 📊 Prediction confidence score
* 🔢 Numerical feature input
* ⚡ Fast prediction
* 📱 Responsive design
* 🛡️ Input validation
* 🚀 Ready for cloud deployment

---

## 🌐 3. Demo

### 🚀 Live Application

> 🔗 **Live Demo:** `Coming Soon`

After deployment, replace the above with your Render URL:

Live Demo = `https://breast-cancer-prediction-pewf.onrender.com/`

### 🖥️ Application Preview

> Add screenshots of your application here after completing the UI and deployment.

```text
📸 Home Page
📸 Prediction Form
📸 Prediction Result
```

---

## 🛠️ 4. Technologies Used

| Technology       | Purpose                   |
| ---------------- | ------------------------- |
| 🐍 Python        | Core programming language |
| 🌐 Flask         | Backend web framework     |
| 🐼 Pandas        | Data processing           |
| 🔢 NumPy         | Numerical computation     |
| 🤖 Scikit-learn  | Machine learning          |
| 🌳 Random Forest | Classification algorithm  |
| 🎨 Tailwind CSS  | Frontend styling          |
| 🧾 HTML          | Web page structure        |
| 🔧 Git           | Version control           |
| 🐙 GitHub        | Source code management    |
| 🚀 Render        | Deployment                |
| ⚡ Gunicorn       | Production WSGI server    |

---

## 🧠 5. Machine Learning Model

This project uses a **Random Forest Classifier** for breast tumor classification.

### 🌳 Random Forest

Random Forest is an ensemble machine learning algorithm that combines multiple decision trees to produce a more robust classification result.

### Model Configuration

```text
Algorithm       : Random Forest Classifier
Estimators      : 500
Random State    : 42
Problem Type    : Binary Classification
Train/Test Split: 80/20
```

### Classification

The model maps the diagnosis column as:

```text
M → Malignant → 1
B → Benign    → 0
```

---

## 📊 6. Dataset

The project uses a breast cancer diagnostic dataset stored in:

```text
breast-cancer-data.csv
```

The dataset contains tumor-related measurements used to train the classification model.

### Selected Features

The current model uses five features:

```text
radius_mean
texture_mean
perimeter_mean
smoothness_mean
compactness_mean
```

These features are provided as numerical inputs to the trained Random Forest model.

---

## 📁 7. Project Structure

```text
Breast_Cancer_Prediction/
│
├── 📄 app.py
├── 📊 breast-cancer-data.csv
├── 📦 requirements.txt
├── 📖 README.md
├── 🚫 .gitignore
│
└── 📂 templates/
    └── 🌐 index.html
```

### File Description

| File                     | Description                               |
| ------------------------ | ----------------------------------------- |
| `app.py`                 | Flask application and ML prediction logic |
| `breast-cancer-data.csv` | Training dataset                          |
| `requirements.txt`       | Python dependencies                       |
| `templates/index.html`   | Frontend user interface                   |
| `.gitignore`             | Files excluded from Git                   |
| `README.md`              | Project documentation                     |

---

## ⚙️ 8. Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/Breast_Cancer_Prediction.git
```

### 2️⃣ Navigate to the Project

```bash
cd Breast_Cancer_Prediction
```

### 3️⃣ Create a Virtual Environment

Windows:

```bash
python -m venv .venv
```

### 4️⃣ Activate Virtual Environment

Windows PowerShell:

```powershell
.venv\Scripts\activate
```

### 5️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ 9. How to Run

Start the Flask application:

```bash
python app.py
```

The application will run locally at:

```text
http://127.0.0.1:5000
```

Open the URL in your browser.

### 🛑 Stop the Application

Press:

```text
CTRL + C
```

in the terminal.

---

## 🔄 10. How It Works

The application follows these steps:

### Step 1 — User Input

The user enters five tumor measurements through the web interface.

### Step 2 — Data Processing

Flask receives the values and converts them into numerical data.

### Step 3 — Feature Preparation

The input is converted into a Pandas DataFrame with the same feature names used during model training.

### Step 4 — Random Forest Prediction

The trained Random Forest model processes the input data.

### Step 5 — Classification

The model predicts:

```text
0 → Benign
1 → Malignant
```

### Step 6 — Confidence

The model's predicted probability is used to display a confidence percentage.

### Step 7 — Result

The prediction is displayed on the web interface.

---

## 🧪 11. Input Features

The application currently accepts the following five features:

| Feature            | Description                  |
| ------------------ | ---------------------------- |
| `radius_mean`      | Mean radius of the tumor     |
| `texture_mean`     | Mean texture measurement     |
| `perimeter_mean`   | Mean perimeter of the tumor  |
| `smoothness_mean`  | Mean smoothness measurement  |
| `compactness_mean` | Mean compactness measurement |

### Example Input

```text
Radius Mean       : 14.2
Texture Mean      : 19.5
Perimeter Mean    : 92.1
Smoothness Mean   : 0.096
Compactness Mean  : 0.104
```

> ⚠️ The example values above are only for demonstrating the input format and should not be interpreted as medical guidance.

---

## 📈 12. Model Evaluation

The dataset is divided into training and testing subsets:

```text
Training Data : 80%
Testing Data  : 20%
```

The model performance is evaluated using **Accuracy Score**.

### Model Accuracy

```text
Accuracy: XX.XX%
```

> Replace `XX.XX%` with the actual accuracy obtained from your model.

### Future Evaluation Metrics

The project can be extended with:

* Accuracy
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC-AUC Score

---

## 🚀 13. Deployment

The application can be deployed using **Render**.

### Deployment Architecture

```text
                    GitHub
                       │
                       ▼
                  ┌─────────┐
                  │  Render │
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │ Gunicorn│
                  └────┬────┘
                       │
                       ▼
                  ┌─────────┐
                  │  Flask  │
                  └────┬────┘
                       │
                       ▼
               Random Forest Model
```

### Build Command

```bash
pip install -r requirements.txt
```

### Start Command

```bash
gunicorn app:app
```

### 🌐 Live URL

* 🐙 Live url=`https://breast-cancer-prediction-pewf.onrender.com/`

Once deployed, add your live application URL here.

---

## 📸 14. Screenshots

Add screenshots of your application here.

### 🏠 Home Page

![App Screenshot](screenshots/Home.png)

### 📝 Prediction Form

![App Screenshot](screenshots/Prediction_form.png)

### 📊 Prediction Result

![App Screenshot](screenshots/Result.png)

### File Structure
```text
Breast_Cancer_Prediction/
│
├── screenshots/
│   ├── home.png
│   ├── prediction-form.png
│   └── result.png
│
├── app.py
├── breast-cancer-data.csv
├── requirements.txt
├── README.md
└── templates/
    └── index.html
```

---

## ⚠️ 15. Limitations

This project has several limitations:

* The model currently uses only five selected features.
* The application is designed primarily for educational and demonstration purposes.
* The model has not been clinically validated.
* Prediction performance depends on the quality and distribution of the training dataset.
* Machine learning predictions should not be treated as definitive medical diagnoses.

---

## 🩺 16. Disclaimer

> **IMPORTANT:** This application is an educational machine learning project and is **not a medical diagnostic system**.

The predictions generated by this application should **not** be used as a substitute for professional medical advice, diagnosis, or treatment.

Always consult a qualified healthcare professional for medical decisions.

---

## 🔮 17. Future Improvements

The project can be improved by adding:

### 🤖 Machine Learning

* [ ] Compare Random Forest with Logistic Regression
* [ ] Add Support Vector Machine
* [ ] Add XGBoost
* [ ] Perform hyperparameter tuning
* [ ] Add cross-validation
* [ ] Add ROC-AUC analysis
* [ ] Add confusion matrix visualization

### 📊 Data Science

* [ ] Exploratory Data Analysis dashboard
* [ ] Feature importance visualization
* [ ] Correlation analysis
* [ ] Outlier detection
* [ ] Feature selection

### 🌐 Web Application

* [ ] User authentication
* [ ] Prediction history
* [ ] Interactive charts
* [ ] Better error handling
* [ ] API endpoint
* [ ] Mobile optimization

### ☁️ Deployment

* [ ] Production monitoring
* [ ] Custom domain
* [ ] CI/CD pipeline
* [ ] Docker support

---

## 👨‍💻 18. Author

### Rupesh Kumar

**MCA — Artificial Intelligence & Machine Learning**

Interested in:

```text
💻 Full Stack Development
🤖 Artificial Intelligence
📊 Data Science
🧠 Machine Learning
```

### Connect With Me

* 🐙 GitHub: `https://github.com/rupeshkumar96`
* 💼 LinkedIn: `https://www.linkedin.com/in/rupesh-kumar12`

---

## 📄 19. License

This project is available for educational and learning purposes.

You can add an MIT License to the repository if you want to make the project openly reusable.

```text
MIT License
```

---

<p align="center">

### ⭐ If you found this project useful, consider giving it a star!

**Made with ❤️ by Rupesh Kumar**

</p>
