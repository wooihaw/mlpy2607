# Scale data (between 0 and 1)
import numpy as np
from pandas import read_csv
from sklearn.preprocessing import MinMaxScaler
df = read_csv('data/heights_weights_genders.csv')
# Separate into features and target
X = df.drop(columns=['Gender'])
y = df['Gender']
scaler = MinMaxScaler(feature_range=(0, 1))
scaler.fit(X)
scaledX = scaler.transform(X)
# Check min and max of all column
print(f'minimum={np.min(scaledX, axis=0)}, maximum={np.max(scaledX, axis=0)}')