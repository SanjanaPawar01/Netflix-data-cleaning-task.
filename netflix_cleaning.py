import pandas as pd

# Step 1: Load the Data
df = pd.read_csv(r'C:\Users\PC\Desktop\Task\task\netflix_titles.csv')

# Step 2: Print the first 5 rows to check the data
print(df.head())

# Step 3: Check missing values
print(df.isnull().sum())

# Step 4: Fill missing text values with 'Unknown'
df['director'] = df['director'].fillna('Unknown')
df['cast'] = df['cast'].fillna('Unknown')
df['country'] = df['country'].fillna('Unknown')
df['rating'] = df['rating'].fillna('Unknown')

# Step 5: Remove rows with missing 'date_added' or 'duration'
df = df.dropna(subset=['date_added', 'duration'])

# Step 6: Check missing values again
print(df.isnull().sum())

# Step 7: Remove duplicates
print("Number of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()

# Step 8: Clean the 'type' column (convert to lowercase and strip extra spaces)
df['type'] = df['type'].str.lower().str.strip()

# Step 9: Optional - Fix specific inconsistencies in the 'type' column (e.g., 'tv show' to 'TV Show')
df['type'] = df['type'].replace('tv show', 'TV Show')

# Step 10: Create dummies (One-Hot Encoding) for the 'type' column
if 'type' in df.columns:
    df = pd.get_dummies(df, columns=['type'], prefix='type')
    print("Dummies created successfully.")
else:
    print("'type' column not found!")

# Step 11: Save the cleaned dataset to a new CSV file
df.to_csv('cleaned_netflix_data.csv', index=False)

# Step 12: Final message
print("Data cleaning is complete, and the file is saved as 'cleaned_netflix_data.csv'")
