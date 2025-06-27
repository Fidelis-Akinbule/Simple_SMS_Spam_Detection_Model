import streamlit as st
import joblib
import string

# Load trained model and vectorizer
model = joblib.load('Data\\ProcessedData\\spam_model.pkl')
vectorizer = joblib.load('Data\\ProcessedData\\tfidf_vectorizer.pkl')

# Function to clean text
def clean_text(text):
    text = text.lower()
    text = ''.join([char for char in text if char not in string.punctuation])
    return text

# Streamlit UI
st.title("📩 SMS Spam Classifier")
st.write("Enter a message below and see whether it's **Spam** or **Not Spam**.")

user_input = st.text_area("Your message", "")

if st.button("Predict"):
    cleaned = clean_text(user_input)
    vec = vectorizer.transform([cleaned])
    prediction = model.predict(vec)[0]
    if prediction == 1:
        st.error("🚨 This message is **Spam**")
    else:
        st.success("✅ This message is **Not Spam**")
