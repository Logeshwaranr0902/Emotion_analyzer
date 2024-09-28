from flask import Flask, request, jsonify
import joblib
import pandas as pd
import numpy as np
import string
import nltk
from flask_cors import CORS


app = Flask(__name__)
CORS(app) 


model = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\emotion_classification_model(20k-randomforest).pkl')
vectorizer = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\vectorizer(20k-randomforest).pkl')


def preprocess_text(text):
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation))  
    tokens = text.split()  
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  
    return ' '.join(tokens)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    if file:
    
        df = pd.read_csv(file)

    
        df['cleaned_comments'] = df['text'].apply(preprocess_text)

       
        new_comments_vectorized = vectorizer.transform(df['cleaned_comments'])

        
        predictions = model.predict(new_comments_vectorized)

        
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

       
        return jsonify(emotion_results)

if __name__ == '__main__':
    app.run(debug=True)
