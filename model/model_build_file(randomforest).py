import pandas as pd
import nltk
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("started")

nltk.download('stopwords')
print("finished")


def preprocess_text(text):
    text = text.lower()  
    text = text.translate(str.maketrans('', '', string.punctuation))  
    tokens = text.split()  
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  
    return ' '.join(tokens)

print("iamhere")

df = pd.read_parquet(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\train-00000-of-00001 .parquet") 
print("iamhere2")


df['cleaned_comments'] = df['text'].apply(preprocess_text) 
print("Preprocessing data...")


X = df['cleaned_comments'] 
print("iamhere3")
y = df['label']  
print("iamhere4")


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
print("Vectorizing data...")


model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vectorized, y_train)
print("Training model...")


y_pred = model.predict(X_test_vectorized)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']))


joblib.dump(model, 'emotion_classification_model(20k-randomforest).pkl')
joblib.dump(vectorizer, 'vectorizer(20k-randomforest).pkl')
