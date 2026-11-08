import seaborn as sns
import matplotlib.pyplot as plt

restaurant_df = sns.load_dataset('tips')
restaurant_df = restaurant_df.dropna()

print("First 5 rows:")
print(restaurant_df.head())
print()

print(restaurant_df.info())
print()

print(restaurant_df.describe())
print()

print("Days available:", restaurant_df['day'].unique())

sns.histplot(data=restaurant_df, x='total_bill', bins=15, color='yellow')
plt.title('Distribution of Total Bill')
plt.xlabel('Total Bill ($)')
plt.ylabel('Count')
plt.show()

sns.kdeplot(data=restaurant_df, x='tip', fill=True, color='purple')
plt.title('Tip Amount Pattern (KDE)')
plt.xlabel('Tip ($)')
plt.show()

sns.histplot(data=restaurant_df, x='tip', kde=True, color='teal')
plt.title('Tip Amount — Histogram with KDE Curve')
plt.xlabel('Tip ($)')
plt.ylabel('Count')
plt.show()

sns.scatterplot(
    data=restaurant_df,
    x='total_bill',
    y='tip',
    hue='day'
)
plt.title('Total Bill vs Tip by Day')
plt.xlabel('Total Bill ($)')
plt.ylabel('Tip ($)')
plt.show()

matrix_corr = restaurant_df.corr(numeric_only=True)

print("Correlation table:")
print(matrix_corr)
print()

sns.heatmap(matrix_corr, annot=True, cmap='Blues')
plt.title('Correlation Heatmap — Restaurant Tips Data')
plt.show()