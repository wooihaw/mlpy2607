# Use read_csv() to load data from CSV file
from pandas import read_csv
df = read_csv('data/cdc_diabetes_small.csv')
print(df.head(3)) # print the first 3 rows of data
# separate data into features and target
X = df.drop(columns=['Diabetes_binary'])
y = df['Diabetes_binary']
print(df.shape, X.shape, y.shape) # print the dimension of the dataframe, X & y