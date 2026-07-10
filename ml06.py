import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Load the dataset
df = pd.read_csv('data/cdc_diabetes_small.csv')
# Histogram
df['Age'].hist()
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Plotting boxplots for the features
df.boxplot(column=['GenHlth', 'MentHlth', 'PhysHlth', 'Age', 'Education', 'Income'])
plt.title('Box plot')
plt.show()

# Scatter Plot
df.plot.scatter(x='Age', y='BMI')
plt.title('Scatter plot of Age vs BMI')
plt.xlabel('Age')
plt.ylabel('BMI')
plt.show()

# Correlation Heatmap
features = df.columns
plt.figure(figsize=(10, 6))
plt.imshow(df.corr(), cmap='hot', interpolation='nearest')
plt.colorbar()
plt.title('Correlation Heatmap')
plt.xticks(ticks=np.arange(len(features)), labels=features, rotation='vertical')
plt.yticks(ticks=np.arange(len(features)), labels=features)
plt.tight_layout()
plt.show()

# Density Plot
df['BMI'].plot(kind='density')
plt.title('Density Plot of BMI')
plt.xlabel('BMI')
plt.show()

# Pie Chart
df['Diabetes_binary'].value_counts().plot(kind='pie', autopct='%.1f%%')
plt.title('Class Distribution')
plt.show()