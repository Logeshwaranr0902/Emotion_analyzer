from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import string
import nltk
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # To allow cross-origin requests

# Load the saved model and vectorizer
model = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\emotion_classification_model(20k-randomforest).pkl')
vectorizer = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\vectorizer(20k-randomforest).pkl')

# Preprocessing function
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Tokenize
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
        # Load CSV into DataFrame
        df = pd.read_csv(file)

        # Preprocess text
        df['cleaned_comments'] = df['text'].apply(preprocess_text)

        # Vectorize text
        new_comments_vectorized = vectorizer.transform(df['cleaned_comments'])

        # Predict emotions
        predictions = model.predict(new_comments_vectorized)

        # Count occurrences of each emotion
        emotion_counts = np.bincount(predictions, minlength=6)
        emotion_dict = {
            0: 'sadness',
            1: 'joy',
            2: 'love',
            3: 'anger',
            4: 'fear',
            5: 'surprise'
        }
        emotion_results = {emotion_dict[i]: int(count) for i, count in enumerate(emotion_counts)}

        # Return the results as JSON
        return jsonify(emotion_results)

if __name__ == '__main__':
    app.run(debug=True)
