from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
emails = ['win money now', 'hello friend', 'claim free prize', 'meeting at 5 pm']
labels = ['spam', 'ham', 'spam', 'ham']
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(emails)
model = MultinomialNB()
model.fit(X, labels)
test_email = ['free money prize']
test_vector = vectorizer.transform(test_email)
print('Prediction:', model.predict(test_vector)[0])