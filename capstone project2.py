import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

print(sns.get_dataset_names())
df = sns.load_dataset("planets")

print(df.shape)
print(df.head())
print(df.tail())
print(df.info())
print(df.dtypes)
print(df.isnull().sum())
print(df.describe())
print(df.describe(include="all"))

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.show()

df.select_dtypes(include=[np.number]).hist(figsize=(10,8))
plt.show()

print(df['method'].value_counts())

plt.figure(figsize=(10, 5))
sns.countplot(x="method", data=df)
plt.title("Planets Count by Discovery Method")
plt.xticks(rotation=45)  
plt.show()

sns.pairplot(data=df, hue="method")
plt.show()