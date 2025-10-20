'''

Soit A un tableau de n entiers

1- algo itératif qui calcule la somme des élémant de A
déterminer la complexité

2 - algo récursif qui calcul la somme des éléments de A
déterminer la complexité

'''

def sommeIteratif(A):
    r = int()
    for i in range(len(A)):
        r += A[i]
    return r

def sommeRecursif(A, i):
    if i == len(A):
        return 0
    return A[i] + sommeRecursif(A, i + 1)


if __name__ == '__main__':
    tableau = [10, 22, 5, 75, 65, 80]
    print(sommeIteratif(tableau))
    print(sommeRecursif(tableau, 0))