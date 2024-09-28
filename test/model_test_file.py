import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk


model = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\emotion_classification_model(20k-randomforest).pkl')
vectorizer = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\vectorizer(20k-randomforest).pkl')


new_comments_df = pd.read_csv(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\test_dataset.csv")  


def preprocess_text(text):
    text = text.lower() 
    text = text.translate(str.maketrans('', '', string.punctuation)) 
    tokens = text.split() 
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  
    return ' '.join(tokens)
new_comments_df['cleaned_comments'] = new_comments_df['text'].apply(preprocess_text)


new_comments_vectorized = vectorizer.transform(new_comments_df['cleaned_comments'])


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
emotion_counts_df = pd.DataFrame({
    'Emotion': [emotion_dict[i] for i in range(len(emotion_counts))],
    'Count': emotion_counts
})


plt.figure(figsize=(10, 6))
sns.barplot(data=emotion_counts_df, x='Emotion', y='Count', hue='Emotion', palette='viridis', legend=False)
plt.title('Emotion Distribution of Comments')
plt.xlabel('Emotion')
plt.ylabel('Number of Comments')
plt.show()
