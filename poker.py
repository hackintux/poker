# Couleurs du texte
class Colors:
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'  # Fin de la couleur

def saisir_position():
    positions_valides = ["bt", "sm", "bb", "utg", "hj", "co"]
    position = input("Veuillez saisir votre position à la table  : ")

    while position.lower() not in positions_valides:
        print("Position invalide ! Veuillez réessayer.")
        position = input("Veuillez saisir votre position à la table : ")

    return position.lower()

def saisir_main():
    main_joueur = []

    for i in range(2):
        valeur_carte = input("Veuillez saisir la valeur de la carte n°{} de votre main (2-10, J, Q, K, A) : ".format(i+1))
        couleur_carte = input("Veuillez saisir la couleur de la carte n°{} de votre main (C, K, T, P) : ".format(i+1))
        carte = valeur_carte.upper() + couleur_carte[0].upper()  # Convertir en majuscules et concaténer valeur et couleur
        main_joueur.append(carte)

    return main_joueur

position_joueur = saisir_position()
main_joueur = saisir_main()

print(Colors.BLUE + "Position du joueur :", position_joueur + Colors.ENDC)
print(Colors.BLUE + "Main du joueur :", main_joueur)

def verifier_meme_couleur(main):
    if main[0][-1] == main[1][-1]:
        return True
    else:
        return False

def verifier_meme_valeur(main):
    if main[0][:-1] == main[1][:-1]:
        return True
    else:
        return False

if verifier_meme_valeur:
    print(Colors.GREEN + "Continue" + Colors.ENDC)
else:
    print(Colors.FAIL + "Stop" + Colors.ENDC)

