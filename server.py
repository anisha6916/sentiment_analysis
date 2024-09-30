from flask import Flask, request, url_for, redirect, render_template, jsonify
import joblib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

classifier = joblib.load('classifier.joblib')
vectorizer = joblib.load('vectorizer.joblib')

#@app.route("/")
#def home():
  #return render_template('index.html')

@app.route('/predict', methods = ['POST'])
def sentiment():
  data = request.get_json()
  sentence = data.get('sentence', '')
  simple_test = [sentence]
  #vectorizer = CountVectorizer()
  simple_test_dtm = vectorizer.transform(simple_test)
  prediction = classifier.predict(simple_test_dtm)
  return jsonify({"prediction": str(prediction)})
  #reponse = jsonify({ "statusCode": 200, "status": "Prediction made", "result": "the sentiment is: " + str(prediction)})
  #return render_template('index.html', prediction_text = 'The sentiment prediction is {}'.format(prediction))
#print(sentiment())

if __name__ == "__main__":
    app.run(debug=True)
