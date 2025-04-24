

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from datetime import datetime

sns.set(style='whitegrid')


df = pd.read_csv('flights_sample.csv')
df.head()
     


# Convert FlightDate to datetime
df['FlightDate'] = pd.to_datetime(df['FlightDate'])

# Remove cancelled flights
df = df[df['Cancelled'] == 0]
df.shape
     


# Average delay per airline
airline_delay = df.groupby('Airline')['DepDelayMinutes'].mean().sort_values(ascending=False)
plt.figure(figsize=(10, 5))
airline_delay.plot(kind='bar', color='skyblue')
plt.title('Average Departure Delay per Airline')
plt.ylabel('Delay (minutes)')
plt.xlabel('Airline')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
     

# Delays by hour of day
df['Hour'] = pd.to_datetime(df['ScheduledDepTime'], format='%H:%M').dt.hour
hourly_delay = df.groupby('Hour')['DepDelayMinutes'].mean()
plt.figure(figsize=(10, 5))
hourly_delay.plot(kind='line', marker='o')
plt.title('Average Departure Delay by Hour of Day')
plt.ylabel('Delay (minutes)')
plt.xlabel('Hour')
plt.grid(True)
plt.tight_layout()
plt.show()
