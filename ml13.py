# Robust scaling (0 median, 1 IQR)
import numpy as np
from sklearn.preprocessing import RobustScaler
from pandas import read_csv
df = read_csv('data/heights_weights_genders.csv')
# Separate into features and target
X = df.drop(columns=['Gender'])
y = df['Gender']
scaler = RobustScaler()
scaledX = scaler.fit_transform(X)
# Check median and IQR of all columns
q3, q1 = np.percentile(scaledX, [75 ,25], axis=0)
print(f'median={np.median(scaledX, axis=0)}, IQR={q3-q1}')