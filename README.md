🚀 Features

Classifies emails as ✅ Legitimate or 🚨 Phishing

Confidence score with probability breakdown

Highlights suspicious keywords (red) and URLs (orange) inside email text

Simple Streamlit web app for real-time testing

Built using Logistic Regression + TF-IDF

📂 Project Structure
phishing_email_detector/
│── data/
│    └── phishing_email.csv
│── models/
│    ├── phishing_model.pkl
│    └── vectorizer.pkl
│── modules/
│    ├── preprocessing.py   # Data cleaning + vectorization
│    ├── trainer.py         # Train and evaluate model
│    └── predict.py         # Test predictions on sample email
│── app.py                  # Streamlit app
│── requirements.txt
│── README.md

⚙️ Setup Instructions
1. Clone repo & install requirements
git clone https://github.com/<your-username>/phishing_email_detector.git
cd phishing_email_detector
pip install -r requirements.txt

2. Train the model
python -m modules.trainer


This creates:

models/phishing_model.pkl

models/vectorizer.pkl

3. Run the Streamlit app
streamlit run app.py

🧪 Example

Input:

Dear User, Your account has been suspended. 
Click here https://fake-login.com to verify your credentials immediately.


Output:

🚨 Phishing detected with 95% confidence

Highlighted suspicious words and URL

📊 Dataset

Source: Public phishing email dataset (Kaggle).

~82,000 emails with text and label columns.

Labels: 0 = Legit, 1 = Phishing.

🌐 Live Demo (if deployed)

👉 Try it on Streamlit Cloud

🔮 Future Improvements

Support .eml file upload

Add “Why flagged?” explanations (feature importance)

Train transformer-based model (BERT/DistilBERT)

Dataset used: Phishing Email Dataset on Kaggle