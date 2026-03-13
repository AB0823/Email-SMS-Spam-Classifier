# 📩 SMS Spam Classifier
A Machine Learning web application that detects whether an SMS message is Spam or Not Spam using Natural Language Processing (NLP) and Naive Bayes classification.
The model processes the input text, converts it into numerical features using TF-IDF, and predicts whether the message is spam.

# 🚀 Live Demo

🔗 App Link:
https://email-sms-spam-classifier-1dbf12b16c21.herokuapp.com/

# 🧠 Project Overview

Spam messages often contain patterns such as promotional offers, prizes, or urgent requests.
This project uses NLP techniques and machine learning models to automatically detect such messages.

The pipeline includes:
Text Input
   ->
Text Preprocessing
->
Tokenization + Stopword Removal
   ->
Lemmatization
   ->
TF-IDF Vectorization
   ->
Naive Bayes Model
   ->
Spam / Not Spam Prediction

# 🛠️ Technologies Used
  Python,
  Streamlit,
  NLTK,
  Scikit-learn,
  Pandas,
  NumPy

-> Key techniques used:
  Natural Language Processing (NLP),
  TF-IDF Feature Extraction,
  Naive Bayes Classification
  
# 🔎 Machine Learning Model

Three Naive Bayes models were evaluated:

Model	Accuracy
  GaussianNB	~86%,
  MultinomialNB	~97%,
  BernoulliNB	~98%,

The Bernoulli Naive Bayes model achieved the best performance and was selected for deployment.

# ⚙️ Features

✔ Spam message detection
✔ Clean and interactive Streamlit UI
✔ NLP preprocessing pipeline
✔ TF-IDF feature engineering
✔ Machine learning model deployment
✔ Real-time prediction

