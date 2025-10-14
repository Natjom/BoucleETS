import kagglehub
import pandas as pd
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("lakshmi25npathi/bike-sharing-dataset")
print("Path to dataset files:", path)

df = pd.read_csv(f"{path}/day.csv")

print(df.head())
print("\nColonnes :", df.columns)

df = df.rename(columns={
    'dteday': 'date',
    'cnt': 'total_rides',
    'temp': 'temp_norm',
    'hum': 'humidity',
    'windspeed': 'wind_speed'
})

df['date'] = pd.to_datetime(df['date'])

print("\nStatistiques :")
print(df[['temp_norm', 'humidity', 'wind_speed', 'total_rides']].describe())

plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['total_rides'], label='Total des locations', linewidth=1)
plt.title("Évolution quotidienne des locations de vélos (2011-2012)")
plt.xlabel("Date")
plt.ylabel("Nombre de locations")
plt.legend()
plt.show()

df['weekday'] = df['weekday'].replace({
    0: 'Dimanche', 1: 'Lundi', 2: 'Mardi', 3: 'Mercredi',
    4: 'Jeudi', 5: 'Vendredi', 6: 'Samedi'
})

mean_by_day = df.groupby('weekday')['total_rides'].mean().reindex([
    'Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi', 'Samedi', 'Dimanche'
])

plt.figure(figsize=(10, 5))
mean_by_day.plot(kind='bar', color='skyblue')
plt.title("Moyenne des locations par jour de la semaine")
plt.ylabel("Nombre moyen de locations")
plt.show()

best_days = mean_by_day.sort_values(ascending=False)
print("\nJours les plus propices à l’ouverture du service :")
print(best_days)

corr = df[['temp_norm', 'humidity', 'wind_speed', 'total_rides']].corr()
print("\nCorrélation entre météo et usage :")
print(corr)
