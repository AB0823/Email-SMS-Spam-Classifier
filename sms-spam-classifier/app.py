import nltk
import streamlit as st
import pickle
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

st.set_page_config(
    page_title="SMS Spam Detector",
    page_icon="📩",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #f5f7fa, #c3cfe2);
}

textarea {
    font-size:16px !important;
}

.big-font {
    font-size:18px !important;
}

</style>
""", unsafe_allow_html=True)

st.markdown(
"""
<h1 style='text-align: center; color: #2E86C1;'>
📩 SMS Spam Classifier
</h1>
<p style='text-align: center; font-size:18px;'>
Detect whether a message is <b>Spam</b> or <b>Not Spam</b>
</p>
""",
unsafe_allow_html=True
)

lemma = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum() and i not in stop_words:
            y.append(lemma.lemmatize(i,pos='v'))
    return " ".join(y)

tf = pickle.load(open('vectorizer.pkl','rb'))
model =  pickle.load(open('model.pkl','rb'))

input_sms = st.text_area(
    "✉️ Enter your message",
    height=150,
    placeholder="Type or paste your SMS message here..."
)

col1, col2, col3 = st.columns([1,1,1])

with col2:
    predict = st.button("🔍 Analyze Message")

if predict:
    with st.spinner("Analyzing message..."):
        transformed_sms = transform_text(input_sms)
        vector_input = tf.transform([transformed_sms])
        result = model.predict(vector_input)[0]
        if result == 0:
            st.success("✅ Not Spam")
        else:
            st.error("🚨 Spam Message")

st.markdown("---")

st.markdown(
"<p style='text-align:center'>Built with ❤️ using Streamlit</p>",
unsafe_allow_html=True
)