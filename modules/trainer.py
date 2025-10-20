import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from modules.preprocessing import load_and_preprocess

def train_model():
    X_train, X_test, y_train, y_test, vectorizer = load_and_preprocess()

    # Train Logistic Regression
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)

    # Evaluate
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    print("✅ Accuracy:", acc)
    print(classification_report(y_test, y_pred))

    # Save model + vectorizer
    joblib.dump(model, "models/phishing_model.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    print("✅ Model and vectorizer saved in 'models/' folder")

if __name__ == "__main__":
    train_model()
