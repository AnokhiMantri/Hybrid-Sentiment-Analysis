import streamlit as st
import pickle
import numpy as np
import plotly.graph_objects as go

from emoji_engine import calculate_emoji_score
from fusion_engine import hybrid_prediction

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(
    page_title="Hybrid Sentiment Analyzer",
    page_icon="🤖",
    layout="wide"
)

# ---------------------------
# CUSTOM CSS
# ---------------------------
st.markdown("""
<style>
.main {
    background: linear-gradient(to right, #1e3c72, #2a5298);
}
.stTextArea textarea {
    border-radius: 10px;
}
.stButton button {
    border-radius: 10px;
    height: 3em;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# LOAD MODEL
# ---------------------------
model = pickle.load(open("../models/model.pkl", "rb"))
vectorizer = pickle.load(open("../models/vectorizer.pkl", "rb"))

# ---------------------------
# TITLE
# ---------------------------
st.title("🤖 Hybrid Sentiment Analysis System")
st.markdown("### Multi-Class Sentiment Detection (Text + Emoji Intelligence)")

# ---------------------------
# TABS
# ---------------------------
tab1, tab2 = st.tabs(["📝 Text + Emoji Mode", "📊 Probability Analytics"])

with tab1:
    user_input = st.text_area("Enter your text with emojis:", height=150)

    if st.button("Analyze Sentiment"):

        if user_input.strip() == "":
            st.warning("Please enter some text.")
        else:
            # Vectorize text
            text_vector = vectorizer.transform([user_input])
            text_probs = model.predict_proba(text_vector)[0]

            # Emoji score
            emoji_score, emoji_count = calculate_emoji_score(user_input)

            # Hybrid Prediction
            final_label, adjusted_probs = hybrid_prediction(
                text_probs, emoji_score
            )

            confidence = np.max(adjusted_probs) * 100

            st.success(f"Final Sentiment: **{final_label.upper()}**")
            st.info(f"Confidence: {confidence:.2f}%")
            st.write(f"Emoji Count Detected: {emoji_count}")
            st.write(f"Emoji Score: {emoji_score}")

with tab2:
    if 'adjusted_probs' in locals():
        labels = ["Negative", "Neutral", "Positive"]

        fig = go.Figure(
            data=[go.Bar(
                x=labels,
                y=adjusted_probs,
                text=[f"{p*100:.2f}%" for p in adjusted_probs],
                textposition='auto'
            )]
        )

        fig.update_layout(
            title="Hybrid Model Probability Distribution",
            yaxis_title="Probability",
            xaxis_title="Sentiment Class"
        )

        st.plotly_chart(fig, width="stretch")

    else:
        st.info("Analyze some text first to see probability distribution.")
