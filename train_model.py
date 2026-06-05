import pandas as pd
import joblib

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline

data = pd.read_csv("gender_data.csv")

X = data["Name"]
y = data["Gender"]

model = Pipeline([
    ('vectorizer', CountVectorizer(analyzer='char')),
    ('classifier', MultinomialNB())
])

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model trained and saved successfully!")