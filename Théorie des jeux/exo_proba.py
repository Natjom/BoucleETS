import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

n = 5
p = 0.6

prob = 1 - binom.cdf(2, n, p)

print(f"Probabilité qu'au moins 3 jours aient une couverture nuageuse < 50% : {prob:.4f}")

x = np.arange(0, n + 1)
y = binom.pmf(x, n, p)

plt.bar(x, y, color='red')
plt.title("Distribution Binomiale : Nombre de jours avec couverture < 50%")
plt.xlabel("Nombre de jours favorables (sur 5)")
plt.ylabel("Probabilité")
plt.show()
