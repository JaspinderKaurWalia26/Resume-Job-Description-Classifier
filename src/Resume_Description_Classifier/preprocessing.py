import re
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def preprocess_text(text):
    #Cleaning text
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    # tokenization
    tokens = text.split()
    # lowercasing
    tokens = [word.lower() for word in tokens]
    # Removing stopwords
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)

