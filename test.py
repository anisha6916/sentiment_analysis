import joblib
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

classifier = joblib.load('classifier.joblib')
vectorizer = joblib.load('vectorizer.joblib')

simple_test = ['Enjoyed watching it with my daughter']
simple_test_dtm = vectorizer.transform(simple_test)
prediction = classifier.predict(simple_test_dtm)
print(prediction)
