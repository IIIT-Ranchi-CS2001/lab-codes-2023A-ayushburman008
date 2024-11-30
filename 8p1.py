import numpy as np
import matplotlib.pyplot as plt

# Dataset
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000],  # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020],  # Day 5
    [1800, 2300, 2100, 1500, 1050],  # Day 6
    [1900, 2400, 2200, 1600, 1100],  # Day 7
])

countries = ["Country_A", "Country_B", "Country_C", "Country_D", "Country_E"]

# Task 1: Basic Statistics
total_cases_per_country = covid_data.sum(axis=0)
country_with_highest_total = countries[np.argmax(total_cases_per_country)]

# Task 2: Daily Analysis
average_cases_per_day = covid_data.mean(axis=1)
day_with_highest_total_cases = np.argmax(covid_data.sum(axis=1)) + 1

# Task 3: Trends
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
country_with_highest_increase = countries[np.argmax(percentage_change)]

# Task 4: Data Transformation
normalized_data = (covid_data - covid_data.min(axis=0)) / (covid_data.max(axis=0) - covid_data.min(axis=0))

# Visualization
days = np.arange(1, 8)

plt.figure(figsize=(10, 6))

# Line chart for daily cases per country
for i, country in enumerate(countries):
    plt.plot(days, covid_data[:, i],label = country, marker='o')

# Highlight the day with the highest total cases
highest_day_total = np.max(covid_data.sum(axis=1))
plt.axvline(x=day_with_highest_total_cases, color='red', linestyle='--', alpha=0.7)
plt.annotate(f"Day {day_with_highest_total_cases} (Total: {highest_day_total})", 
             xy=(day_with_highest_total_cases, highest_day_total),
             xytext=(day_with_highest_total_cases + 0.5, highest_day_total - 500),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

plt.title("Daily COVID-19 Cases per Country")
plt.xlabel("Day")
plt.ylabel("Number of Cases")
plt.legend()
plt.grid(True)
plt.show()

# Output results
print("Total cases per country:", total_cases_per_country)
print("Country with the highest total cases:", country_with_highest_total)
print("Average cases per day across all countries:", average_cases_per_day)
print("Day with the highest total across all countries:", day_with_highest_total_cases)
print("Percentage change in case from Day 1 to Day 7:", percentage_change)
print("Country with the highest percentage increase:", country_with_highest_increase)
print("Normalized dataset:\n", normalized_data)
