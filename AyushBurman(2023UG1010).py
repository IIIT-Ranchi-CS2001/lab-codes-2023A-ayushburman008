import pandas as pd
import numpy as np

df=pd.read_csv("AQI_Data.csv")

print("First 5 rows:")
print(df.head(5))

print("\nLast 6 rows:")
print(df.tail(6))

print("\nSummary statistics for all numeric columns:")
print(df.describe())

mean_aqi=np.mean(df['AQI'])
mean_pm25=np.mean(df['PM2.5'])
mean_pm10=np.mean(df['PM10'])

print(f"\nMean AQI value: {mean_aqi}")
print(f"Mean PM2.5 value: {mean_pm25}")
print(f"Mean PM10 value: {mean_pm10}")

city_aqi=dict(zip(df['City'], df['AQI']))

city_max=max(city_aqi, key=city_aqi.get)
max_aqi=city_aqi[city_max]

city_min=min(city_aqi, key=city_aqi.get)
min_aqi=city_aqi[city_min]

print(f"City with the highest AQI: {city_max} (AQI: {max_aqi})")
print(f"City with the lowest AQI: {city_min} (AQI: {min_aqi})")