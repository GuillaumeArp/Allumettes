import random

def matches_game():
    print("""
    Il y a un tas de 50 allumettes.
    Le but du jeu est de retirer de 1 à 6 allumettes à chaque tour,
    et être le dernier à retirer la dernière allumette.
    """)
    nb_matches = 50
    num_list = ["1", "2", "3", "4", "5", "6"]

    while nb_matches > 0:
      print(f"Joueur : il reste {nb_matches} allumettes")
      matches_removed = input("Entrez un nombre d'allumettes à retirer entre 1 et 6: ")
      if matches_removed in num_list:
        if int(matches_removed) <= nb_matches:
          nb_matches -= int(matches_removed)
        else:
          print("Il n'est pas possible de retirer plus d'allumettes que le nombre restant")
          continue
      else:
        print("Veuillez choisir un entier entre 1 et 6")
        continue
      if nb_matches == 0:
        print("Bravo, vous avez retiré la dernière allumette !")
        break

      print(f"Bot : il reste {nb_matches} allumettes")
      if nb_matches >= 6:
        matches_removed_bot = random.randint(1, 6)
        print(f"Le bot a choisi de retirer {matches_removed_bot} allumettes")
      else:
        matches_removed_bot = random.randint(1, nb_matches)
        print(f"Le bot a choisi de retirer {matches_removed_bot} allumettes")
      nb_matches -= matches_removed_bot
      if nb_matches == 0:
        print("Perdu, le bot a retiré la dernière allumette !")
        break
    

matches_game()