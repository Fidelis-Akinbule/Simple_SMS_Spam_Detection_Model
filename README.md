# 📩 SMS Spam Detection with Machine Learning

This project is an end-to-end machine learning application that classifies SMS messages as **Spam** or **Not Spam**. It uses a trained model and is deployed using **Streamlit** for a simple, interactive web interface.

---

## 📁 Project Structure

```

.
├── app.py                                           # Streamlit app for spam classification
|-- Data\\Raw\\spam.csv                              # Raw file
├── Data\\ProcessedData\\spam_model.pkl              # Trained machine learning model
├── Data\\ProcessedData\\tfidf_vectorizer.pkl        # TF-IDF vectorizer used during training
├── SMS_Spam_Detection_project.ipynb                 # Jupyter notebook (training & evaluation)
└── README.md                                        # Project documentation

````

---

## 🚀 Features

- Clean and preprocess raw SMS text data
- Convert text into numerical features using **TF-IDF Vectorization**
- Train a classifier (e.g., Naive Bayes or similar)
- Evaluate model performance (accuracy, precision, recall, F1-score)
- Deploy a simple **Streamlit** app to test the model with custom input

---

## 🧠 Technologies Used

- Python 🐍
- Pandas, NumPy – data manipulation
- Scikit-learn – model training and evaluation
- Streamlit – web app interface
- Joblib – saving and loading models

---

## 🛠️ Setup Instructions

### 1. Clone the repository or download the project files

Make sure the following files are in the same directory:
- `app.py`
- `spam_model.pkl`
- `tfidf_vectorizer.pkl`

### 2. Set up a virtual environment (recommended)

```bash
python -m venv spamEnv
spamEnv\Scripts\activate  # On Windows
# source spamEnv/bin/activate  # On macOS/Linux
````

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not provided, install manually:

```bash
pip install streamlit pandas scikit-learn joblib
```

---

## ▶️ Running the App

To launch the Streamlit app:

```bash
streamlit run app.py
```

Then open the link in your browser (usually [http://localhost:8501](http://localhost:8501)).

---

## 📓 Notebook Overview

The Jupyter notebook (`SMS Spam Detection project.ipynb`) contains:

* Data loading and exploration
* Text preprocessing (lowercasing, punctuation removal)
* TF-IDF vectorization
* Model training and evaluation
* Saving the model and vectorizer

---

## 🧪 Example Use

**Input:**

```
Congratulations! You’ve won a free ticket to Bahamas! Reply ‘YES’ to claim now.
```

**Output:**

```
🚨 This message is Spam
```

---

## 📦 Exported Artifacts

* `spam_model.pkl`: Trained classifier
* `tfidf_vectorizer.pkl`: Fitted TF-IDF transformer

These are used in the Streamlit app for prediction.

---

## 📌 Future Improvements

* Use NLP libraries like NLTK or spaCy for advanced preprocessing
* Add message length or other features to improve accuracy
* Deploy to cloud (e.g., Heroku, Streamlit Cloud)
* Include model confidence score

---

## 👤 Author

**Fidelis Akinbule**


[[Linkedin] (https://LinkedIn.com/in/Fidelis-akinbule | [[GitHub] (https://github.com/Fidelis-Akinbule/Simple_SMS_Spam_Detection_Model.git)]

