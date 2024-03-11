from flask import Flask, request, jsonify
import pickle
from model import perform_sentiment_analysis

app = Flask(__name__)

# Load the SentimentIntensityAnalyzer model
with open('sia.pkl', 'rb') as f:
    sia_model = pickle.load(f)


@app.route('/')
def index():
    return 'Welcome to Sentiment Analysis App!'


@app.route('/sentiment', methods=['POST'])
def sentiment():
    word = request.form.get('word')
    positive_headlines, negative_headlines, plot_path = perform_sentiment_analysis(word)

    # Return the results as JSON
    return jsonify({
        'positive_headlines': list(positive_headlines),
        'negative_headlines': list(negative_headlines),
        'plot_path': plot_path
    })


if __name__ == '__main__':
    app.run(debug=True)
