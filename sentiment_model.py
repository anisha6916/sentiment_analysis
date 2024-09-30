import pandas as pd
#path = "/content/Sentiment.csv"
ds = pd.read_csv("Sentiment.csv")
ds = ds[['sentiment', 'text']]
ds.head()
ds.shape[0]

df = pd.DataFrame(ds)
negative_df = df[df["sentiment"] == "Negative"]
negative_df.shape[0]
len(negative_df) / len(ds)

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report
import joblib

train_data, test_data, train_labels, test_labels = train_test_split(df['text'], df['sentiment'], test_size=0.2, random_state=42)


vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_data)
test_features = vectorizer.transform(test_data)

classifier = MultinomialNB()
classifier.fit(train_features, train_labels)

predictions = classifier.predict(test_features)

#accuracy = accuracy_score(test_labels, predictions)
#report = classification_report(test_labels, predictions)
joblib.dump(classifier, 'classifier.joblib')
joblib.dump(vectorizer, 'vectorizer.joblib')


