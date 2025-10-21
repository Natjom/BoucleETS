def trouver_d(e, phi_n):
    for d in range(1, phi_n):
        if (e * d) % phi_n == 1:
            return d
    return None

def dechiffrer_rsa(message_chiffre, n, e):
    p, q = None, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    phi_n = (p - 1) * (q - 1)
    d = trouver_d(e, phi_n)
    message_dechiffre = ""
    for c in message_chiffre:
        m = pow(c, d, n)
        caractere = chr(m)
        message_dechiffre += caractere
    return message_dechiffre

def dechiffrer_rsa_generique(message_chiffre, n, e):
    p, q = None, None
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            p = i
            q = n // i
            break
    phi_n = (p - 1) * (q - 1)
    d = trouver_d(e, phi_n)
    message_dechiffre = ""
    for c in message_chiffre:
        m = pow(c, d, n)
        message_dechiffre += chr(m)
    return message_dechiffre

if __name__ == '__main__':
    C = [2726, 1313, 1992, 884, 2412, 1453, 1230, 2185, 2412, 1992, 1313, 1230, 884,
         1992, 281, 1632, 281, 2170, 1453, 1992, 1230, 2185, 2160, 1230, 1992, 745,
         1632, 1992, 612, 745, 1632, 1627, 2160, 1313, 1992, 2412, 2185, 2160, 2923, 1313]
    n = 3233
    e = 17
    message = dechiffrer_rsa(C, n, e)
    print(f"Message : {message}")