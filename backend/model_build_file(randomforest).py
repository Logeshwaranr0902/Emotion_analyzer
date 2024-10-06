import pandas as pd
import nltk
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("started")
# Download NLTK stopwords
nltk.download('stopwords')
print("finished")

# Function to preprocess text
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Tokenize
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

print("iamhere")
# Load the dataset from a parquet file
df = pd.read_parquet(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\train-00000-of-00001 .parquet")  # Replace with your dataset path
print("iamhere2")

# Preprocess the comments
df['cleaned_comments'] = df['text'].apply(preprocess_text)  # Adjust column name as necessary
print("Preprocessing data...")

# Prepare features and labels
X = df['cleaned_comments']  # Features
print("iamhere3")
y = df['label']  # Labels (0: sadness, 1: joy, 2: love, 3: anger, 4: fear, 5: surprise)
print("iamhere4")

# Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text
vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)
print("Vectorizing data...")

# Train the model using Random Forest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vectorized, y_train)
print("Training model...")

# Evaluate the model
y_pred = model.predict(X_test_vectorized)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=['sadness', 'joy', 'love', 'anger', 'fear', 'surprise']))

# Save the trained model and vectorizer
joblib.dump(model, 'emotion_classification_model(20k-randomforest).pkl')
joblib.dump(vectorizer, 'vectorizer(20k-randomforest).pkl')
