import seaborn as sns 
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df = df.dropna()
print(df.head())
print(df.info())
sns.barplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill ($)")
plt.show()

sns.countplot(x="day", hue="sex", data=df)
plt.title("Number of diners per day by gender")
plt.xlabel("day")
plt.ylabel("count")
plt.show()

sns.boxplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill ($)")
plt.show()

sns.stripplot(x="day", y="total_bill",  data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill ($)")
plt.show()

sns.swarmplot(x="day", y="total_bill",data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill ($)")
plt.show()

sns.jointplot(x="total_bill", y="tip", data=df)
plt.title("total bill vs tip")
plt.show()

sns.jointplot(x="total_bill", y="tip", data=df, kind= "kde")
plt.title("total bill vs tip")
plt.show()

sns.pairplot(df[["total_bill", "tip", "size"]])
plt.title("total bill vs tip vs size")
plt.show()

sns.pointplot(x="day" , y="total_bill", hue="sex",data=df)
plt.title("Average total bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill ($)")
plt.show()

sns.lmplot(x="total_bill", y="tip", data=df)
plt.title("total bill vs tip")
plt.show()

              




