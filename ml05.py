# Print statistical summary and class breakdown
from pandas import read_csv
df = read_csv('data/cdc_diabetes_small.csv')
print(df.describe())  # print the statistical summary of the data
class_counts = df.groupby('Diabetes_binary').size()
print(class_counts)  # print the class breakdown of the data