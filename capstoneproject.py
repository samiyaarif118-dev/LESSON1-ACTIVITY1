import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
print(sns.get_dataset_names())

df = sns.load_dataset("penguins")
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

df.select_dtypes(include=[np.number]).hist(figsize=(12,8))
plt.show()

print(df.sex.value_counts())
print(df.species.value_counts())
print(df.island.value_counts())

sns.countplot(x="sex", data=df)
plt.show()
sns.countplot(x="species", data=df)
plt.show()
sns.countplot(x="island", data=df)
plt.show()

sns.pairplot(data=df, hue="species")
plt.show()


