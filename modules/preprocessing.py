import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

def clean_text(text):
    """Basic text cleaning: remove links, numbers, special chars."""
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', ' link ', text)   # replace links
    text = re.sub(r'\d+', ' number ', text)            # replace numbers
    text = re.sub(r'[^a-z\s]', '', text)               # keep only letters
    return text

def load_and_preprocess(path="data/phishing_email.csv"):
    df = pd.read_csv(path)

    print("Columns in dataset:", df.columns.tolist())

    # Adjust column names to match your CSV
    # (Update these names after checking with df.columns)
    if "text" in df.columns and "label" in df.columns:
        df["clean_text"] = df["text"].apply(clean_text)
        y = df["label"]
    else:
        raise ValueError("Expected 'text' and 'label' columns in dataset")

    X_train, X_test, y_train, y_test = train_test_split(
        df["clean_text"], y, test_size=0.2, random_state=42, stratify=y
    )

    vectorizer = TfidfVectorizer(max_features=5000, stop_words="english")
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)

    return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer

# Quick test
if __name__ == "__main__":
    X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess()
    print("Train shape:", X_train.shape, " Test shape:", X_test.shape)
