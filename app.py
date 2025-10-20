import streamlit as st
import joblib
import re
from modules.preprocessing import clean_text

# Suspicious keywords
SUSPICIOUS_KEYWORDS = [
    "verify", "password", "click here", "login", "update", "bank",
    "account", "suspended", "credentials", "urgent", "payment"
]

def highlight_keywords(text: str):
    """Highlight suspicious keywords in red and links in orange."""
    highlighted = text

    # Highlight suspicious words in red
    for word in SUSPICIOUS_KEYWORDS:
        pattern = re.compile(rf"\b{word}\b", re.IGNORECASE)
        highlighted = pattern.sub(f"**:red[{word}]**", highlighted)

    # Highlight URLs in orange
    url_pattern = re.compile(r'(https?://\S+|www\.\S+)')
    highlighted = url_pattern.sub(lambda m: f"**:orange[{m.group(0)}]**", highlighted)

    return highlighted


# Load model + vectorizer
@st.cache_resource
def load_model():
    model = joblib.load("models/phishing_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

model, vectorizer = load_model()

# Streamlit UI
st.set_page_config(page_title="AI Phishing Email Detector", page_icon="📧", layout="centered")

st.title("📧 AI-Powered Phishing Email Detector")
st.write("Paste an email below to check if it's **phishing** or **legit**")

# Input box
email_text = st.text_area("✉️ Email content:", height=200, placeholder="Paste the email body here...")

if st.button("🔍 Analyze Email"):
    if email_text.strip():
        clean = clean_text(email_text)
        features = vectorizer.transform([clean])

        prediction = model.predict(features)[0]
        proba = model.predict_proba(features)[0]

        label_map = {0: "legit", 1: "phishing"}
        pred_label = label_map.get(int(prediction), "unknown")

        if pred_label == "phishing":
            st.error(f"🚨 Warning: This email is **PHISHING** (Confidence {proba[1]*100:.2f}%)")
        else:
            st.success(f"✅ Safe: This email looks **Legitimate** (Confidence {proba[0]*100:.2f}%)")

        st.write("Confidence breakdown:")
        st.progress(float(proba[1]))  # phishing score bar
        st.json({"Legitimate": f"{proba[0]*100:.2f}%", "Phishing": f"{proba[1]*100:.2f}%"})

        # Show analyzed email with highlights
        st.markdown("### 📑 Email with Suspicious Highlights")
        st.markdown(highlight_keywords(email_text))

    else:
        st.warning("Please paste an email first.")
