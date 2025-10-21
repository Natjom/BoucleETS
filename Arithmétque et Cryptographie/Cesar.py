def cesar(texte: str, decalage: int) -> str:
    resultat = str()
    tableauDecalage = [int(e) for e in texte]
    for i in range(len(tableauDecalage)):
        tableauDecalage[i] = (tableauDecalage[i] + decalage) % 10
    for element in tableauDecalage:
        resultat += str(element)
    return resultat

if __name__ == '__main__':
    texte_encrypte = "9153787770964"
    texte_decrypte = cesar(texte_encrypte, 4)
    print(f"{texte_decrypte[0:2]}°{texte_decrypte[2:4]}'{texte_decrypte[4:6]}.{texte_decrypte[6]}\"N {texte_decrypte[6:8]}°{texte_decrypte[8:10]}'{texte_decrypte[10:12]}.{texte_decrypte[12]}\"W")
