# News Classifier

![News Classification](https://img.shields.io/badge/News%20Classification-Python%20%7C%20Flask%20%7C%20Scikit--learn%20%7C%20Beautiful%20Soup-blue)

## Overview

**News Classifier** is a web application that classifies news articles as real or fake using machine learning algorithms. The application provides a user-friendly interface where users can input URLs or article text to get predictions. It also features a history management system and feedback options to improve accuracy.


![News Classifier Dashboard](https://github.com/omspatil/News-Classifier/blob/6ada1640b7a29449b9d69a20442713e6e67acf1b/New%20Preditor/Images/Dashboard.png)


## Features

- **Real-time Classification**: Input URLs or article text to classify news as real or fake.
- **History Feature**: View and manage past queries.
- **Feedback System**: Provide feedback on classification results to help improve accuracy.
- **Smooth Animations**: Enjoy a modern and interactive user experience.

## Installation

To run this project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/omspatil/News-Classifier.git

2. **Navigate to the project directory**:
   ```bash
   cd News-Classifier
   
3. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   
4. **Run the Flask app**:
   ```bash
   python app.py

## Usage

- Enter a news article URL or paste article text into the input field.
- Click the "Predict" button to receive the prediction.
- Use the history feature to view past queries.
- Provide feedback on the results to help enhance the model.
  
## Dependencies

- Python 3.x
- Flask
- Scikit-learn
- Pandas
- NumPy
- Beautiful Soup
- Requests

## Acknowledgments

- Scikit-learn for providing powerful machine learning algorithms.
- Beautiful Soup for facilitating web scraping.
- Flask for enabling web application development.
- GitHub for hosting the project.

## Model
- The classifier uses a pre-trained machine learning model stored in 'classifier.pkl'.
- It is trained on a dataset of news articles labeled as real or fake.
- The model's performance can be improved by retraining with new data.

## Contributing

Feel free to submit issues or pull requests if you would like to contribute to the project.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## File Structure

```plaintext
News-Classifier/
│
├── app.py               # Main Flask application script
├── requirements.txt     # Python dependencies
├── static/
│   │   └── styles.css   # Custom styles for the application
├── templates/
│   ├── index.html       # Main HTML template for the app
├── New Preditor/
│   └── Images/
│       └── Dashboard.png  # Screenshot of the application dashboard
└── models/
    └── classifier.pkl   # Pre-trained model for news classification

