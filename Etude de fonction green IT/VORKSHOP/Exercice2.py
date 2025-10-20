''''

2 matrices carrées A et B d'ordre n
A * B = C défini par :
Somme de k(=1) à n -> A_i,k * B_k,j

1- Algo calculant produit des 2 sous forme d'un tableau à deux dimensions
calculer complexité / dans quel cas cette complexité est obtenue

2- modifier l'algoritme précédent lorsque la matrice A est de dimension (m*n) et la matrice B de dimension (n*p)
Quelle est la complexité de l'algorithme

'''


def produitMatricesCarres(A: list, B: list) -> list:
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C

def produitMatrices(A: list, B: list) -> list:

    n, m, p = len(A), len(B), len(B[0])
    C = [[0 for _ in range(p)] for _ in range(n)]

    for i in range(n):
        for j in range(p):
            for k in range(m):
                C[i][j] += A[i][k] * B[k][j]
    return C


if __name__ == '__main__':
    A = [[0, 1, 2], [8, 0, 3], [2, 4, 6]]
    B = [[7, 4, 6], [3, 1, 5], [4, 7, 2]]
    C = [[6, 8, 2], [8, 6, 1]]

    for ligne in produitMatricesCarres(A, B):
        print(ligne)

    print()

    for ligne in produitMatrices(A, C):
        print(ligne)

    '''
    La complexité temporelle du produit de deux matrices carrées d’ordre n est en O(n³).
    Dans le cas général de matrices de dimensions (m×n) et (n×p), la complexité est en O(mnp).
    Cette complexité est atteinte lorsque les trois boucles s’exécutent intégralement, c’est-à-dire lorsque les matrices sont denses (aucun élément nul exploitable).
    '''

