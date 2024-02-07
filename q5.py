import pandas as pd
import matplotlib.pyplot as plt

# Read the dataset
df = pd.read_csv("person_info.csv", index_col="ID")

# Convert 'Weight' and 'Height' to numeric, replace null values with mean
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')
mean_weight = df['Weight'].mean()
mean_height = df['Height'].mean()
df['Weight'].fillna(mean_weight, inplace=True)
df['Height'].fillna(mean_height, inplace=True)

# Calculate BMI
df['BMI'] = df['Weight'] / (df['Height'] ** 2) * 100

# Assign obesity level
def classify_obesity(bmi):
    if bmi <= 3:
        return "Underweight"
    elif bmi > 3 and bmi <= 5:
        return "Normal"
    else:
        return "Overweight"

df['Obesity'] = df['BMI'].apply(classify_obesity)

# Draw a bar chart
obesity_counts = df['Obesity'].value_counts()
obesity_counts.plot(kind='bar', xlabel='Obesity Level', ylabel='Count')
plt.title('Obesity Level Distribution')
plt.show()

# Save the modified DataFrame back to CSV file
df.to_csv("modified_person_info6.csv")