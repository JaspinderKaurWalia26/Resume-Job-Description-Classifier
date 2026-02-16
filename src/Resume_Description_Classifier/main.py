import pandas as pd
import logging
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.metrics import (
    confusion_matrix,
    classification_report,
    ConfusionMatrixDisplay
)

from .train_model import train_resume_model
from .predict import predict_resume_category
from .logger import setup_logging


# Setup logging
setup_logging()

# Load dataset
logging.info("Loading dataset")
data = pd.read_csv("data/resume.csv")
logging.info("Dataset loaded successfully")

# Train model
model, vectorizer, X_test, y_test = train_resume_model(data)

# Predictions
y_pred = model.predict(X_test)

# Testing results
logging.info("Classification Report:")
logging.info("\n" + classification_report(y_test, y_pred))
# Test accuracy 
accuracy = accuracy_score(y_test, y_pred)
logging.info(f"Test Accuracy: {accuracy}")

# Sample prediction
sample_text = "Developed responsive web apps using React and JavaScript"
result = predict_resume_category(sample_text, model, vectorizer)
logging.info(f'Predicted Category:{result}')

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=model.classes_
)
disp.plot(cmap="Blues")
plt.title("Resume Classification Confusion Matrix")
plt.savefig("data/confusion_matrix.png")
plt.show()


