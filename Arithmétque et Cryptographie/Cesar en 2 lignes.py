texte_decrypte = (''.join(map(str, [str((int(e) + 4) % 10) for e in "9153787770964"])))
print(f"{texte_decrypte[0:2]}°{texte_decrypte[2:4]}'{texte_decrypte[4:6]}.{texte_decrypte[6]}\"N {texte_decrypte[6:8]}°{texte_decrypte[8:10]}'{texte_decrypte[10:12]}.{texte_decrypte[12]}\"W")


