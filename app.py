from flask import Flask, request, render_template, jsonify
from transformers import pipeline


app = Flask(__name__)


classifier = pipeline("sentiment-analysis")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    text = request.form['text']  # جلب النص من الـ form
    result = classifier(text)
    sentiment = result[0]['label']
    return render_template('index.html', result=sentiment)


if __name__ == '__main__':
    app.run(debug=True)
