import pandas as pd
import sqlite3


# Load Data
df = pd.read_csv("owid-covid-data.csv")

# View first few rows
print("Raw Data Preview:")
print(df.head())

# Data Cleaning
# Remove aggregates, show just country
df = df[df['continent'].notna()]

# Remove irrelevent columns
columns_to_keep = [
    'location', 'continent', 'date',
    'total_cases', 'new_cases',
    'total_deaths', 'new_deaths',
    'people_vaccinated', 'population'
]
df = df[columns_to_keep]

# Handing Missing Null values
# 1. Fill zero for missing values
df.fillna(0, inplace=True)

# 2. Forward-fill (useful for time series)
df = df.sort_values(['location', 'date'])
df.fillna(method='ffill', inplace=True)

# 3. Drop rows with missing data in key columns
df.dropna(subset=['total_cases', 'total_deaths'], inplace=True)

# Convert date to date format
df['date'] = pd.to_datetime(df['date'])

# Rename columns (optional for clarity)
df.rename(columns={'people_vaccinated': 'vaccinated'}, inplace=True)

# Export Cleaned Data to csv
df.to_csv("cleaned_covid_data.csv", index=False)

# Maths
df['death_rate'] = df['total_deaths'] / df['total_cases']
df['vaccinated_ratio'] = df['vaccinated'] / df['population']


# View cleaned dataset
print("Cleaned Data Preview:")
print(df.head())

# Save cleaned data to SQLite database
conn = sqlite3.connect("covid.db")
df.to_sql("covid_data", conn, if_exists="replace", index=False)
conn.close()

print("Data saved to SQLite database: covid.db")


