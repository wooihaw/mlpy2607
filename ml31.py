# Voting Classifier
from pandas import read_csv
from sklearn.model_selection import train_test_split as split
from sklearn.ensemble import VotingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
df = read_csv('data/cdc_diabetes_small.csv')
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
X_train, X_test, y_train, y_test = split(X, y, test_size=0.25, random_state=42)

clf1 = LogisticRegression()
clf2 = GaussianNB()
clf3 = SVC()
vtc = VotingClassifier(estimators=[('lgr', clf1), ('gnb', clf2), ('svc', clf3)], voting='hard')
vtc.fit(X_train, y_train)
print(f"Accuracy: {vtc.score(X_test, y_test):.2%}")