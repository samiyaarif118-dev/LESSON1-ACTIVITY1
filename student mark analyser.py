import pandas as pd

print("CLASS 10 SCIENCE & MATH PERFORMANCE")


print("\nPART 1: Pandas Series")

scores = [92, 81, 74, 88, 95]

top_scores = pd.Series(
    scores,
    index=["Priya", "Rahul", "Simran", "Amit", "Neha"]
)

print(top_scores)

print("\nPART 2: Pandas DataFrame")

data = {
    "Student": ["Priya", "Rahul", "Simran", "Amit", "Neha"],
    "Math": [92, 81, 74, 88, 95],
    "Science": [89, 76, 82, 90, 94],
    "English": [94, 85, 79, 84, 91],
    "Project": [90, 88, 85, 92, 96]
}

df = pd.DataFrame(data)

print(df)

print("\nPART 3: Reading Data from a CSV File")

df.to_csv("class_performance.csv", index=False)

student_data = pd.read_csv("class_performance.csv")

print("CSV file generated and read successfully!")
print(student_data)

print("\nPART 4: Viewing Data")

print("\nTop 3 students (First 3 rows):")
print(student_data.head(3))

print("\nBottom 2 students (Last 2 rows):")
print(student_data.tail(2))

print("\nDataset Summary Information:")
print(student_data.info())

print("\nPART 5: Cleaning Data")

messy_data = {
    "Student": ["Priya", "Rahul", "Simran", "Amit", "Neha"],
    "Math": [92, None, 74, 88, 95],
    "Science": [89, 76, None, 90, 94],
    "English": [94, 85, 79, None, 91]
}

messy_df = pd.DataFrame(messy_data)

print("\nDataset containing missing values (None):")
print(messy_df)

cleaned_df = messy_df.fillna(50)

print("\nCleaned Dataset (Missing values replaced with 50):")
print(cleaned_df)

print("\nPART 6: Student Total and Average Scores")

cleaned_df["Total"] = cleaned_df["Math"] + cleaned_df["Science"] + cleaned_df["English"]
cleaned_df["Average"] = cleaned_df["Total"] / 3

print(cleaned_df)
