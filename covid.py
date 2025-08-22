import pandas as pd

file_path = r"C:\Users\DLIB-12\Downloads\covidfolder\coviddeathbycountry.csv"

df = pd.read_csv(file_path)
# Display the first few rows
print(df.head())

# Display dataset information
print(df.info())
df['Deaths'] = pd.to_numeric(df['Deaths'], errors='coerce')
df['Cases'] = pd.to_numeric(df['Cases'], errors='coerce')
df.fillna(0, inplace=True)

import matplotlib.pyplot as plt

# Group by 'Country' and sum 'Cases' and 'Deaths'
country_summary = df.groupby('Country')[['Cases', 'Deaths']].sum()

# Sort by 'Cases' in descending order
top_countries = country_summary.sort_values(by='Cases', ascending=False).head(10)

# Plot
top_countries.plot(kind='bar', figsize=(10, 6))
plt.title("Top 10 Countries by Confirmed COVID-19 Cases")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

import seaborn as sns

# Plotting the correlation
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Cases', y='Deaths', data=df)
plt.title("Correlation Between COVID-19 Cases and Deaths")
plt.xlabel("Number of Cases")
plt.ylabel("Number of Deaths")
plt.tight_layout()
plt.show()

# Find the country with the highest number of cases
max_cases_country = df.loc[df['Cases'].idxmax()]
print("Country with the highest number of cases:")
print(f"{max_cases_country['Country']}: {max_cases_country['Cases']} cases, {max_cases_country['Deaths']} deaths")





