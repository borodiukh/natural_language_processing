import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# 0 not spam
# 1 spam

# load the data
headers = ['label', 'message']
data = pd.read_csv('emails_ds.csv', sep=';', names=headers, encoding='utf-8')
# print(data)


X = data['message']
Y = data['label']
# print(X)
# print(Y)

# convert the emails message
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(X)
# print(X)

# split data into training and testing
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

# train the logistic regression model
model = LogisticRegression()
model.fit(X_train, Y_train)

# prediction on the test set
Y_pred = model.predict(X_test)


print(f'Accuracy: {accuracy_score(Y_test, Y_pred)}')
print(f'Precision: {precision_score(Y_test, Y_pred)}')
print(f'Recall: {recall_score(Y_test, Y_pred)}')
print(f'F1: {f1_score(Y_test, Y_pred)}')

