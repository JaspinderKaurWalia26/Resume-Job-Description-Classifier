from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from .preprocessing import preprocess_text
import logging

def train_resume_model(data):
    # Text preprocessing
    data["cleaned_text"] = data["resume_text"].apply(preprocess_text)
    logging.info("Text preprocessing completed")

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=5000)
    X = vectorizer.fit_transform(data["cleaned_text"])
    y = data["category"]

    # Train-test splitting
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Model training
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    logging.info("Model training completed")

    return model, vectorizer, X_test, y_test
