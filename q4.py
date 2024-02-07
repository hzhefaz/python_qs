import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file and set ID as the index column
df = pd.read_csv("person_info.csv", index_col="ID")

# Convert 'Weight' and 'Height' to numeric, replace null values with mean
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

mean_weight = df['Weight'].mean()
mean_height = df['Height'].mean()

df['Weight'] = df['Weight'].fillna(mean_weight)
df['Height'] = df['Height'].fillna(mean_height)

# Calculate BMI and assign obesity level
df['BMI'] = df['Weight'] / (df['Height'] ** 2) * 100

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

# Write the modified DataFrame back to CSV file
df.to_csv("modified_person_info4.csv")
