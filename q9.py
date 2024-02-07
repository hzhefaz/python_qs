import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("person_info.csv", index_col="ID")

# Convert Weight and Height to numeric, replace null values with mean
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
df['Weight'].fillna(df['Weight'].mean(), inplace=True)
df['Height'].fillna(df['Height'].mean(), inplace=True)

# Create a new column BMI
df['BMI'] = df['Weight'] / (df['Height'] ** 2) * 100

# Make another column "Obesity"
def classify_obesity(bmi):
    if bmi <= 3:
        return "Underweight"
    elif bmi > 3 and bmi <= 5:
        return "Normal"
    else:
        return "Overweight"

df['Obesity'] = df['BMI'].apply(classify_obesity)

# Draw a bar chart of Obesity column
obesity_counts = df['Obesity'].value_counts()
obesity_counts.plot(kind='bar', xlabel='Obesity Level', ylabel='Count')
plt.title('Obesity Level Distribution')
plt.show()

# Write the modified DataFrame back to CSV file
df.to_csv("modified_person_infppo.csv")
