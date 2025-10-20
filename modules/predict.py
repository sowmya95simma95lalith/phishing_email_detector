import joblib
from modules.preprocessing import clean_text

def load_model():
    model = joblib.load("models/phishing_model.pkl")
    vectorizer = joblib.load("models/vectorizer.pkl")
    return model, vectorizer

def predict_email(email_text: str):
    """Predict if an email is phishing or legitimate."""
    model, vectorizer = load_model()

    # Preprocess email
    clean = clean_text(email_text)
    features = vectorizer.transform([clean])

    # Prediction
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    return prediction, proba

if __name__ == "__main__":
    test_email = """
    Dear User, Your account has been suspended. 
    Click here http://suspicious-link.com to verify your credentials immediately.
    """
    prediction, proba = predict_email(test_email)
    print(f"Prediction: {prediction}")
    print(f"Confidence: Legit={proba[0]:.2f}, Phishing={proba[1]:.2f}")
