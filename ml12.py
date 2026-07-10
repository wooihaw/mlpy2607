# Standardize data (0 mean, 1 stdev)
import numpy as np
from sklearn.preprocessing import StandardScaler
from pandas import read_csv
df = read_csv('data/heights_weights_genders.csv')
# Separate into features and target
X = df.drop(columns=['Gender'])
y = df['Gender']
scaler = StandardScaler()
scaledX = scaler.fit_transform(X)
# Check mean and standard deviation of all columns
print(f'mean={np.mean(scaledX, axis=0)}, variance={np.var(scaledX, axis=0)}')
