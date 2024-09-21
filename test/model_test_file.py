import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk

# Load the saved model and vectorizer
model = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\emotion_classification_model(20k-randomforest).pkl')
vectorizer = joblib.load(r'C:\Users\Logeshwaran\Downloads\emotion_detection\model\vectorizer(20k-randomforest).pkl')

# Load the new dataset
new_comments_df = pd.read_csv(r"C:\Users\Logeshwaran\Downloads\emotion_detection\Resources\test_dataset.csv")  # Adjust as needed

# Preprocess the comments
def preprocess_text(text):
    text = text.lower()  # Convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation))  # Remove punctuation
    tokens = text.split()  # Tokenize
    tokens = [word for word in tokens if word not in nltk.corpus.stopwords.words('english')]  # Remove stopwords
    return ' '.join(tokens)
new_comments_df['cleaned_comments'] = new_comments_df['text'].apply(preprocess_text)

# Vectorize the new comments
new_comments_vectorized = vectorizer.transform(new_comments_df['cleaned_comments'])

# Predict emotions
predictions = model.predict(new_comments_vectorized)

# Count occurrences of each emotion
emotion_counts = np.bincount(predictions, minlength=6)

# Create a DataFrame for counting
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

# Set up the bar plot
plt.figure(figsize=(10, 6))
sns.barplot(data=emotion_counts_df, x='Emotion', y='Count', hue='Emotion', palette='viridis', legend=False)
plt.title('Emotion Distribution of Comments')
plt.xlabel('Emotion')
plt.ylabel('Number of Comments')
plt.show()
