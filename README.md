This project consists of a full-stack web application for emotion analysis. The frontend, built using React, allows users to upload a CSV file containing text data, which is then processed and analyzed. The uploaded text undergoes a preprocessing step, where it's cleaned of stopwords and punctuation. The React app utilizes axios to send the text data to a Flask backend, where a pre-trained RandomForest model predicts the emotions expressed in the text. The backend uses pandas for CSV processing and scikit-learn for text vectorization. The predicted results are then visualized as a bar chart on the frontend using Recharts. Additionally, the application supports both light and dark modes for enhanced user experience.
![App Screenshot](Screenshot%202024-09-22%20212110.png)

![App Screenshot](Screenshot%202024-09-22%20212648.png)
![App Screenshot](Screenshot%202024-09-22%20214826.png)

