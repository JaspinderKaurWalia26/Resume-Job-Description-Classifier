from .preprocessing import preprocess_text

def predict_resume_category(text, model, vectorizer):
    cleaned_text = preprocess_text(text)
    text_vector = vectorizer.transform([cleaned_text])
    prediction = model.predict(text_vector)[0]
    return prediction

