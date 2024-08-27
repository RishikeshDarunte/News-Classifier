from flask import Flask, render_template, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
import os

app = Flask(__name__)

# this will Load the datasets
true_df = pd.read_csv('Data\True.csv')
true_df['label'] = 0

fake_df = pd.read_csv('Data\Fake.csv')
fake_df['label'] = 1

df = pd.concat([true_df, fake_df], ignore_index=True)

# Balance the dataset
true_news_count = df['label'].value_counts()[0]
fake_news_count = df['label'].value_counts()[1]
if true_news_count > fake_news_count:
    true_df = true_df.sample(fake_news_count)
else:
    fake_df = fake_df.sample(true_news_count)
df = pd.concat([true_df, fake_df], ignore_index=True)

# Split data
X_train, X_test, y_train, y_test = train_test_split(df['text'], df['label'], test_size=0.2, random_state=42)

# Train model
pipeline = make_pipeline(TfidfVectorizer(stop_words='english'), MultinomialNB())
pipeline.fit(X_train, y_train)

# Save model
joblib.dump(pipeline, 'news_classifier_model.pkl')

# Load model
model = joblib.load('news_classifier_model.pkl')

# Load persistent files if they exist
if os.path.exists('true_news.txt'):
    with open('true_news.txt', 'r') as file:
        true_news_feedback = file.readlines()
else:
    true_news_feedback = []

if os.path.exists('fake_news.txt'):
    with open('fake_news.txt', 'r') as file:
        fake_news_feedback = file.readlines()
else:
    fake_news_feedback = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form.get('text', '').strip()
    if not user_input:
        return jsonify({'prediction': 'Please enter a news article.'})

    # Check if input exists in feedback files
    if user_input + '\n' in true_news_feedback:
        prediction_text = 'The news is likely to be true.'
    elif user_input + '\n' in fake_news_feedback:
        prediction_text = 'The news is likely to be fake.'
    else:
        prediction = model.predict([user_input])[0]
        prediction_text = 'The news is likely to be true.' if prediction == 0 else 'The news is likely to be fake.'
    
    return jsonify({'prediction': prediction_text})

@app.route('/feedback', methods=['POST'])
def feedback():
    user_input = request.form.get('text', '').strip()
    feedback = request.form.get('feedback', '')

    if not user_input or not feedback:
        return jsonify({'status': 'failure', 'message': 'Invalid input'})

    if feedback == 'wrong':
        # Add to fake news file
        with open('fake_news.txt', 'a') as file:
            file.write(user_input + '\n')
        fake_news_feedback.append(user_input + '\n')
    elif feedback == 'correct':
        # Add to true news file
        with open('true_news.txt', 'a') as file:
            file.write(user_input + '\n')
        true_news_feedback.append(user_input + '\n')

    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
