import numpy as np
from scipy.stats import binom


n = 4
p = 0.7

risk_failure = 1 - (p ** n)



risk_failure_check = binom.cdf(3, n, p)

if risk_failure == risk_failure_check:
    print(f"Probabilité d'échec sur les {n} jours : {risk_failure:.4f}")
else:
    print("Le calcul n'est pas bon.")