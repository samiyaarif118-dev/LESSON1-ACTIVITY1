import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("penguins")
df = df.dropna()

print(df.head())
print(df.info())
print(df.describe())

print("species:", df["species"].unique())
print("island:", df["island"].unique())

sns.histplot(data=df, x="body_mass_g", bins=20, color="blue")
plt.title("Distribution of penguin body_mass")
plt.xlabel("body_mass_g")
plt.ylabel("count")
plt.show()

sns.kdeplot(data=df, x="flipper_length_mm", hue="species", fill=True)
plt.title("flipper length distribution by species")
plt.xlabel("flipper_length_mm")
plt.ylabel("density")
plt.show()

sns.scatterplot(data=df, x="flipper_length_mm", y="body_mass_g", hue="species")
plt.title("flipper length vs body mass by species")
plt.xlabel("flipper_length_mm")
plt.ylabel("body_mass_g")
plt.show()

numeric_values = df.corr(numeric_only=True)
sns.heatmap(numeric_values, annot=True, cmap="coolwarm")
plt.title("correlation heatmap of penguin")
plt.show()

