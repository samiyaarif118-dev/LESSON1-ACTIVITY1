import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
df = df.dropna()

print(df.head())
print(df.info())

sns.barplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Average customer bill per day by gender")
plt.xlabel("Day")
plt.ylabel("Average bill($)")
plt.show()

sns.countplot(x="day",hue="sex", data=df)
plt.title("Number of customers per day by gender")
plt.xlabel("Day")
plt.ylabel("Number of customers")
plt.show()

sns.boxplot(x="day",y="total_bill", data=df)
plt.title("spread of customer bill per day")
plt.xlabel("Day")
plt.ylabel("Customer bill($)")
plt.show()

sns.stripplot(x="day",y="total_bill", data=df,jitter=True)
plt.title("Distribution of customer bill per day")
plt.xlabel("Day")
plt.ylabel("Customer bill($)")
plt.show()

sns.swarmplot(x="day", y="total_bill", data=df)
plt.title("Every customer bill per day (Swarm plot)")
plt.xlabel("day")
plt.ylabel("total bill($)")
plt.show()

sns.jointplot(x="total_bill", y="tip", data=df)
plt.title("Customer bill vs tip", y=1.02)
plt.show()

sns.jointplot(x="total_bill", y="tip", data=df, kind="kde")
plt.title("Customer bill vs tip KDE joint plot", y=1.02)
plt.show()

sns.pairplot(df[["total_bill", "tip", "size"]])
plt.title("pair plot bill, tip and party size", y=1.02)
plt.show()

sns.pointplot(x="day", y="total_bill", hue="sex", data=df)
plt.title("Average customer bill per day by gender")
plt.xlabel("day")
plt.ylabel("Average bill($)")
plt.show()

sns.lmplot(x="total_bill", y="tip", data=df)
plt.title("Customer bill vs tip trend line")
plt.show()



