# Resume Text Classifier

This project is a Resume Text Classification system.  
It classifies resumes into different categories using Logistic Regression.

---

## 📂 Project Structure
```
RESUME_TEXT_CLASSIFIER/
│
├── data/
│   ├── resume.csv
│   └── confusion_matrix.png
│
├── logs/
│   └── app.log
│
├── src/
│   └── Resume_Description_Classifier/
│       ├── __init__.py
│       ├── logger.py
│       ├── main.py
│       ├── predict.py
│       ├── preprocessing.py
│       └── train_model.py
│
└── README.md
```
---

## 📊 Dataset

- **File:** `data/resume.csv`
- Contains resume text and their corresponding categories.
- Columns used:
  - `resume_text`
  - `category`
