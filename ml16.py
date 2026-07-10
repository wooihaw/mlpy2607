# Model-based Feature Selection with Random Forest
from pandas import read_csv
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_selection import SelectFromModel
df = read_csv('data/cdc_diabetes_small.csv')
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
selector = SelectFromModel(RandomForestClassifier(random_state=42), threshold='median')
features = selector.fit_transform(X, y)
selected = selector.get_support()
# Show selected features
features = df.columns
print([features[i] for i, j in enumerate(selected) if j])
