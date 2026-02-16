# Resume Text Classifier

This project is a Resume Text Classification system that categorizes resumes into different job domains using a Logistic Regression model.

---

## 📂 Project Structure
```
RESUME_TEXT_CLASSIFIER/
│
├── data/
│   ├── resume.csv      #dataset
│   └── confusion_matrix.png   # confusion matrix
│
├── logs/
│   └── app.log  # log file
│
├── src/
│   └── Resume_Description_Classifier/
│       ├── __init__.py    # marks the initialization
│       ├── logger.py      # logging setup
│       ├── main.py        # main execution file
│       ├── predict.py     # sample text input prediction function
│       ├── preprocessing.py  # preprocessing 
│       └── train_model.py    # model training
│
└── README.md   # project documentation
```
---

---

---

## Project Deliverables

1. **Python Implementation**
   - The complete solution is implemented using Python.
   - The main execution script is:
     ```
     src/Resume_Description_Classifier/main.py
     ```

2. **Dataset Preparation**
   - The dataset used for training and testing is provided in:
     ```
     data/resume.csv
     ```
   - The dataset consists of resume text samples categorized into different job domains.
   - Each resume record contains:
     - Resume content (`resume_text`)
     - Corresponding category (`category`)

3. **Model Training and Testing**
   - The dataset is divided into training and testing sets.
   - Logistic Regression is used for training the classification model.
   - Model performance is evaluated using unseen test data.

4. **Evaluation Metrics**
   - The model evaluation includes:
     - Precision
     - Recall
     - F1-score
     - Accuracy
   - A detailed classification report is generated during testing.

5. **Confusion Matrix**
   - A confusion matrix is generated to visualize the classification performance.
   - The confusion matrix image is stored at:
     ```
     data/confusion_matrix.png
     ```

6. **Prediction Function**
   - A prediction function is implemented to classify new resume text:
     ```python
     predict_resume_category(text)
     ```
   - The function returns the predicted category based on trained model output.

---
## How to Run the Project

1. Install required libraries:
   ```bash
   pip install pandas nltk scikit-learn matplotlib
   ```
2. Run the main file:
   ```bash
   python -m src.Resume_Description_Classifier.main 
   ```

