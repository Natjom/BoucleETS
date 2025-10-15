import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

df = pd.read_csv("server_usage_data.csv")

print("Aperçu du jeu de données :")
print(df.head(), "\n")
print("Infos :")
print(df.info(), "\n")

print("Valeurs manquantes :")
print(df.isna().sum(), "\n")

stats_desc = df.describe()
print("Statistiques descriptives globales :")
print(stats_desc, "\n")

cols = ['CPU_Usage', 'Memory_Usage', 'Network_Usage', 'Temperature']
for col in cols:
    plt.figure(figsize=(8,4))
    plt.hist(df[col], bins=30, color='steelblue', edgecolor='black')
    plt.title(f"Distribution de {col}")
    plt.xlabel(col)
    plt.ylabel("Fréquence")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()

def detect_zscore(series, threshold=3):
    z = np.abs(stats.zscore(series))
    return np.where(z > threshold)[0]

def detect_iqr(series):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return series[(series < lower) | (series > upper)].index

def detect_percentmax(series, pct=0.95):
    threshold = series.max() * pct
    return series[series > threshold].index

print("=== Détection d'anomalies ===")
for col in cols:
    z_anom = len(detect_zscore(df[col]))
    iqr_anom = len(detect_iqr(df[col]))
    pct_anom = len(detect_percentmax(df[col]))
    print(f"{col} : Z-score={z_anom}, IQR={iqr_anom}, >95%max={pct_anom}")

plt.figure(figsize=(10,5))
plt.plot(df['CPU_Usage'], label="CPU Usage", color='gray')
anom_idx = detect_zscore(df['CPU_Usage'])
plt.scatter(anom_idx, df.loc[anom_idx, 'CPU_Usage'], color='red', label="Anomalies (Z-score)")
plt.title("Utilisation du CPU avec anomalies détectées")
plt.xlabel("Temps (index)")
plt.ylabel("Utilisation (%)")
plt.legend()
plt.show()

print("\n=== Interprétation rapide ===")
for col in cols:
    mean = df[col].mean()
    std = df[col].std()
    print(f"{col}: Moyenne {mean:.2f}, Écart-type {std:.2f}")
    if mean > 80:
        print(f"Attention : {col} souvent élevé, possible surcharge.")
    elif mean < 30:
        print(f"{col} généralement faible, marge confortable.")
    else:
        print(f"{col} usage modéré, stable.")
    print()
