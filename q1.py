import pandas as pd

# Read the CSV file and set ID as the index column
df = pd.read_csv("person_info.csv", index_col="ID")

# Convert 'Weight' and 'Height' to numeric
df['Weight'] = pd.to_numeric(df['Weight'], errors='coerce')
df['Height'] = pd.to_numeric(df['Height'], errors='coerce')

# Calculate mean values for 'Weight' and 'Height' excluding null values
mean_weight = df['Weight'].mean()
mean_height = df['Height'].mean()

# Replace null values with mean values
df['Weight'].fillna(mean_weight, inplace=True)
df['Height'].fillna(mean_height, inplace=True)

# Write the modified DataFrame back to CSV file
df.to_csv("modified_person_info.csv")