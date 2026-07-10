# Feature Selection with Univariate Selection
from pandas import read_csv
from sklearn.feature_selection import SelectKBest
# load data
df = read_csv('data/cdc_diabetes_small.csv')
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
selector = SelectKBest(k=11)
features = selector.fit_transform(X, y)
selected = selector.get_support()
# Show selected features
features = df.columns
print([features[i] for i, j in enumerate(selected) if j])
