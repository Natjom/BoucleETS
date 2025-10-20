import csv
import os
import time

def force_brute(s, t):
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if s[i] + s[j] == t:
                return (i, j)
    return None

def table_hachage(s, t):
    vv = {}
    for i, v in enumerate(s):
        c = t - v
        if c in vv:
            return (vv[c], i)
        vv[v] = i
    return None

def mesurer_temps(func, data, target, reps=100):
    start = time.time()
    for _ in range(reps):
        func(data, target)
    return (time.time() - start) / reps


def charger_donnees_csv(nom_fichier):
    with open(nom_fichier, newline='') as f:
        reader = csv.reader(f)
        next(reader, None)
        return [int(val) for row in reader for val in row if val.strip().isdigit()]



def tester_algos(dossier, target=100):
    fichiers = sorted([f for f in os.listdir(dossier) if f.endswith(".csv")])
    print(f"{'Fichier':<20} {'Taille':<10} {'Force brute (s)':<20} {'Table hachage (s)':<20}")
    print("-" * 70)

    for fichier in fichiers:
        chemin = os.path.join(dossier, fichier)
        data = charger_donnees_csv(chemin)

        brute_time = mesurer_temps(force_brute, data, target)
        force_brute(data, target)

        hash_time = mesurer_temps(table_hachage, data, target)
        table_hachage(data, target)

        print(f"{fichier:<20} {len(data):<10} {brute_time:<20.6f} {hash_time:<20.6f}")

if __name__ == "__main__":
    dossier = os.path.join(os.path.dirname(__file__), "GreenIT_data")
    tester_algos(dossier, target=100)
