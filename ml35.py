# Use GridSearchCV with pipeline
from pandas import read_csv
from sklearn.model_selection import train_test_split as split
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.model_selection import KFold, GridSearchCV
from sklearn.pipeline import Pipeline

df = read_csv('data/cdc_diabetes_small.csv')
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
X_train, X_test, y_train, y_test = split(X, y, test_size=0.25, random_state=42)

pipe2 = Pipeline([('scaler', None), ('clf', KNeighborsClassifier())])
params = {}
params['scaler'] = [None, MinMaxScaler(), StandardScaler(), RobustScaler()]
params['clf'] = [KNeighborsClassifier(), LogisticRegression(), SVC()]

kf = KFold(n_splits=5, shuffle=True, random_state=42)
grid = GridSearchCV(pipe2, params, cv=kf, n_jobs=-1, verbose=1)
grid.fit(X_train, y_train)
print(grid.best_params_)

best_pipe = grid.best_estimator_
best_pipe.fit(X_train, y_train)
print(f'Accuracy: {best_pipe.score(X_test, y_test):.2%}')