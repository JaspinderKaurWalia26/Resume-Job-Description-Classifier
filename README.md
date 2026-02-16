# Resume Text Classifier

This project is a Resume Text Classification system that categorizes resumes into different job domains using a Logistic Regression model.

---

## 📂 Project Structure
```
RESUME_TEXT_CLASSIFIER/
│
├── data/
│   ├── resume.csv                # Dataset 
│   └── confusion_matrix.png      # Confusion matrix after testing
│
├── logs/
│   └── app.log                   # Log file 
│
├── src/
│   └── Resume_Description_Classifier/
│       ├── __init__.py           # Marks the package initialization
│       ├── logger.py             # Logging setup
│       ├── main.py               # Main execution script
│       ├── predict.py            # Function for predicting categories from sample text
│       ├── preprocessing.py      # Text preprocessing functions
│       └── train_model.py        # Model training and evaluation
│
├── README.md                     # Project documentation
└── requirements.txt              # Python dependencies

```
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
## How to Run

### 1. Clone the repository
```
git clone https://github.com/JaspinderKaurWalia26/Resume-Job-Description-Classifier.git
cd Resume-Job-Description-Classifier
```
### 2. Create a virtual environment (optional)
```
python -m venv venv
```
### 3. Activate the virtual environment
- Windows:
```
venv\Scripts\activate
```
- Linux/Mac:
```
source venv/bin/activate
```
### 4. Install dependencies
```
pip install -r requirements.txt
```
### 5. Run the program
```
python -m src.Resume_Description_Classifier.main 
```
### 6. Check outputs

- Confusion Matrix: data/confusion_matrix.png

- Logs: logs/app.log
