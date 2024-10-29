import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv(r'C:\Users\priya\OneDrive\Desktop\netflix dataset\movies.csv')

print(data.head())
print(data.shape)
print(data.info())
print(data.describe())
print(data.isnull().sum())
data['ReleaseYear'].hist()
plt.xlabel('ReleaseYear')
plt.ylabel('MovieTitle')
plt.title('Distribution of Netflix Ratings')
plt.show()
