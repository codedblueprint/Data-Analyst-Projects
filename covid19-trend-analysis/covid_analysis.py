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


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load CSV
df = pd.read_csv("cleaned_covid_data.csv")

# Line Chart: New Cases Over Time (Global)
# Sum new cases globally by date
global_cases = df.groupby('date')['new_cases'].sum().reset_index()

plt.figure(figsize=(14, 5))
sns.lineplot(data=global_cases, x='date', y='new_cases')
plt.title("Global Daily New COVID-19 Cases")
plt.xlabel("Month")
plt.ylabel("New Cases")
plt.tight_layout()
plt.show()


# Top 10 Countries by Total Cases
# Total Cases vs. Total Deaths (Log Scale)
latest = df.groupby('location').last().reset_index()
latest = latest[latest['total_cases'] > 0]

plt.figure(figsize=(10, 6))
sns.scatterplot(data=latest, x='total_cases', y='total_deaths', hue='continent')
plt.xscale('log')
plt.yscale('log')
plt.title("Total Cases vs Total Deaths (Log Scale)")
plt.xlabel("Total Cases (log)")
plt.ylabel("Total Deaths (log)")
plt.tight_layout()
plt.show()

# Death Rate vs Vaccination Rate
latest['death_rate'] = latest['total_deaths'] / latest['total_cases']
latest['vaccination_rate'] = latest['vaccinated'] / latest['population']

plt.figure(figsize=(10, 6))
sns.scatterplot(data=latest, x='vaccination_rate', y='death_rate', hue='continent')
plt.title("Death Rate vs Vaccination Rate by Country")
plt.xlabel("Vaccinated % of Population")
plt.ylabel("Death Rate (Total Deaths / Total Cases)")
plt.tight_layout()
plt.show()

# Top 10 Countries by Total Cases
top10 = latest.sort_values(by='total_cases', ascending=False).head(10)

plt.figure(figsize=(10, 5))
sns.barplot(data=top10, y='location', x='total_cases', palette='rocket')
plt.title("Top 10 Countries by Total COVID-19 Cases")
plt.xlabel("Total Cases")
plt.ylabel("Country")
plt.tight_layout()
plt.show()



# Line Chart: Vaccinations per 100 People by Country
# Compute vaccination rate
df['vaccinated_per_100'] = (df['vaccinated'] / df['population']) * 100

# Select countries
countries = ['United States', 'India', 'Germany', 'Brazil', 'United Kingdom']
subset = df[df['location'].isin(countries)]

plt.figure(figsize=(14, 5))
sns.lineplot(data=subset, x='date', y='vaccinated_per_100', hue='location')
plt.title("Vaccinations per 100 People")
plt.xlabel("Date")
plt.ylabel("Vaccination Rate (%)")
plt.tight_layout()
plt.show()

# Bar Chart: Total Cases and Deaths by Continent
# Get latest total by continent
latest = df.groupby(['continent', 'location']).last().reset_index()
continent_totals = latest.groupby('continent')[['total_cases', 'total_deaths']].sum().reset_index()

# Melt for grouped bar chart
melted = continent_totals.melt(id_vars='continent', var_name='Metric', value_name='Count')

plt.figure(figsize=(10, 6))
sns.barplot(data=melted, x='continent', y='Count', hue='Metric')
plt.title("Total Cases and Deaths by Continent")
plt.tight_layout()
plt.show()

# Pie Chart: Share of Fully Vaccinated Population
# Filter to countries with data
latest = df.groupby('location').last().reset_index()
latest = latest[(latest['population'] > 0) & (latest['vaccinated'] > 0)]

# Top 6 vaccinated countries
top_vax = latest.nlargest(6, 'vaccinated')
labels = top_vax['location']
sizes = top_vax['vaccinated'] / top_vax['vaccinated'].sum()

plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
plt.title("Share of Total Vaccinated Population (Top 6 Countries)")
plt.show()

# Correlation Heatmap: GDP vs Vaccination Rate
# Assume GDP has been merged to latest DataFrame
latest['vaccination_rate'] = latest['vaccinated'] / latest['population']
corr = latest[['gdp_per_capita', 'vaccination_rate', 'total_cases', 'total_deaths']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap: GDP, Vaccination, Cases, Deaths")
plt.tight_layout()
plt.show()


# Load GDP dataset
gdp = pd.read_csv("gdp_per_capita.csv")

# Merge with 'latest' DataFrame on 'location'
latest = pd.merge(latest, gdp, on='location', how='left')

# Correlation Heatmap: GDP vs Vaccination Rate
latest['vaccination_rate'] = latest['vaccinated'] / latest['population']
corr = latest[['gdp_per_capita', 'vaccination_rate', 'total_cases', 'total_deaths']].corr()

plt.figure(figsize=(8, 6))
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap: GDP, Vaccination, Cases, Deaths")
plt.tight_layout()
plt.show()
