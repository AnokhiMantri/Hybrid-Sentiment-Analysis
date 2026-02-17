# 🤖 Hybrid Sentiment Analysis System  
### Multi-Class Sentiment Detection using Text + Emoji Intelligence

---

## 📌 Project Overview

This project is a **Hybrid Sentiment Analysis Web Application** that combines:

- 🧠 Machine Learning (TF-IDF + Logistic Regression)
- 😀 Emoji Sentiment Scoring
- 🔄 Probability Adjustment (Fusion Engine)
- 🌐 Interactive Web UI (Streamlit)

It predicts sentiment as:

- 🔴 Negative  
- 🟡 Neutral  
- 🟢 Positive  

By intelligently combining text meaning and emoji emotional intensity.

---

## 🚀 Features

- ✅ Text-based sentiment classification  
- ✅ Emoji emotion scoring  
- ✅ Hybrid probability fusion model  
- ✅ Confidence score display  
- ✅ Probability visualization (Plotly chart)  
- ✅ Clean UI with custom styling  
- ✅ Multi-tab interface  

---

## 🏗️ Project Architecture

Major-Sentiment-Analysis-Hybrid-Project
│
├── app/
│ ├── app.py
│ ├── emoji_engine.py
│ └── fusion_engine.py
│
├── models/
│ ├── model.pkl
│ └── vectorizer.pkl
│
├── data/
│ └── twitter_airline_sentiment.csv
│
├── train_model.py
├── explore_data.py
└── README.md


---

## ⚙️ Technologies Used

- Python 3.12
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Pickle

---

## 🧠 How It Works

### 1️⃣ Text Processing
- Text is vectorized using **TF-IDF**
- Logistic Regression predicts base probabilities

### 2️⃣ Emoji Analysis
- Emojis are extracted
- Each emoji contributes a sentiment score
- Emoji intensity modifies prediction probabilities

### 3️⃣ Fusion Engine
- Adjusts ML probabilities using emoji weight
- Returns final sentiment and confidence

---

## 📊 Model Details

- Algorithm: Logistic Regression  
- Vectorizer: TF-IDF  
- Classes: Negative, Neutral, Positive  
- Dataset: Twitter Airline Sentiment Dataset  

---

## 🖥️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd Major-Sentiment-Analysis-Hybrid-Project


---

## ⚙️ Technologies Used

- Python 3.12
- Streamlit
- Scikit-learn
- Pandas
- NumPy
- Plotly
- Pickle

---

## 🧠 How It Works

### 1️⃣ Text Processing
- Text is vectorized using **TF-IDF**
- Logistic Regression predicts base probabilities

### 2️⃣ Emoji Analysis
- Emojis are extracted
- Each emoji contributes a sentiment score
- Emoji intensity modifies prediction probabilities

### 3️⃣ Fusion Engine
- Adjusts ML probabilities using emoji weight
- Returns final sentiment and confidence

---

## 📊 Model Details

- Algorithm: Logistic Regression  
- Vectorizer: TF-IDF  
- Classes: Negative, Neutral, Positive  
- Dataset: Twitter Airline Sentiment Dataset  

---

## 🖥️ Installation Guide

### 1️⃣ Clone Repository

```bash
git clone <your-repo-link>
cd Major-Sentiment-Analysis-Hybrid-Project

2️⃣ Create Virtual Environment
python -m venv venv

3️⃣ Activate Environment (Windows)
.\venv\Scripts\Activate

4️⃣ Install Dependencies
pip install streamlit scikit-learn pandas numpy plotly

▶️ Run the Application
cd app
streamlit run app.py


Then open:

http://localhost:8501

🧪 Example Input
This airline service was amazing 😍🔥


Output:

Sentiment: Positive

Confidence: 92%

Emoji Count: 2

Probability Distribution Chart



📈 Future Improvements

🔮 Deep Learning Integration (LSTM / BERT)

📂 Bulk CSV Sentiment Analyzer

📊 Real-time Dashboard Analytics

☁️ Cloud Deployment

📱 Mobile Responsive Design