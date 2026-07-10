# Feature Selection with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.tree import DecisionTreeClassifier
df = read_csv('data/cdc_diabetes_small.csv')
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
model = DecisionTreeClassifier(random_state=42)
rfe = RFE(model, n_features_to_select=11)
features = rfe.fit_transform(X, y)
selected = rfe.get_support()
# Show selected features
features = df.columns
print([features[i] for i, j in enumerate(selected) if j])
