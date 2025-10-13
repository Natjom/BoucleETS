import numpy as np

payoffs = np.array([
    [(2, 2), (1, 3), (0, 4)],
    [(3, 1), (4, 4), (2, 5)],
    [(4, 0), (5, 2), (3, 3)]
])

strategies_A = ["Élevée", "Moyenne", "Faible"]
strategies_B = ["Élevée", "Moyenne", "Faible"]

def best_responses_A():
    best = {}
    for j, sB in enumerate(strategies_B):
        gains_A = [payoffs[i, j][0] for i in range(3)]
        max_A = max(gains_A)
        best[sB] = [strategies_A[i] for i, g in enumerate(gains_A) if g == max_A]
    return best

def best_responses_B():
    best = {}
    for i, sA in enumerate(strategies_A):
        gains_B = [payoffs[i, j][1] for j in range(3)]
        max_B = max(gains_B)
        best[sA] = [strategies_B[j] for j, g in enumerate(gains_B) if g == max_B]
    return best

best_A = best_responses_A()
best_B = best_responses_B()

print("Meilleures réponses de A :", best_A)
print("Meilleures réponses de B :", best_B)

nash_equilibria = []
for i, sA in enumerate(strategies_A):
    for j, sB in enumerate(strategies_B):
        if (sA in best_A[sB]) and (sB in best_B[sA]):
            nash_equilibria.append((sA, sB, payoffs[i, j]))

print("\nÉquilibres de Nash trouvés :")
for eq in nash_equilibria:
    print(f"  {eq[0]} / {eq[1]}  → gains {eq[2]}")

