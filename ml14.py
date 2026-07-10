# Create 2 new features
import pandas as pd
df = pd.read_csv('data/heights_weights_genders.csv')
bins = [0, 158, 179, 210] 
labels = ['Short', 'Average', 'Tall']
df['new_feature1'] = pd.cut(df['Height(cm)'], bins=bins, labels=labels)
df['new_feature2'] = df['Weight(kg)'].rolling(window=3).mean()
print(df.head())