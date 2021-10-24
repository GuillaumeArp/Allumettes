import random

def matches_game_multi():
    print("""
    Il y a un tas de 50 allumettes.
    Le but du jeu est de retirer de 1 à 6 allumettes à chaque tour,
    et être le dernier à retirer la dernière allumette.
    """)
    nb_matches = 50
    num_list = ["1", "2", "3", "4", "5", "6"]
    player_1 = input("Joueur 1, entrez votre nom : ")
    player_2 = input("Joueur 2, entrez votre nom : ")

    while nb_matches > 0:
      print(f"\nTour de {player_1} : il reste {nb_matches} allumettes")
      matches_removed = input(f"{player_1}, entrez un nombre d'allumettes à retirer entre 1 et 6: ")
      if matches_removed in num_list:
        if int(matches_removed) <= nb_matches:
          nb_matches -= int(matches_removed)
        else:
          print(f"Il n'est pas possible de retirer plus d'allumettes que le nombre restant {player_1}.")
          continue
      else:
        print("Veuillez choisir un entier entre 1 et 6")
        continue
      if nb_matches == 0:
        print(f"Bravo {player_1}, vous avez retiré la dernière allumette !")
        break

      print(f"\nTour de {player_2} : il reste {nb_matches} allumettes")
      matches_removed = input(f"{player_2}, entrez un nombre d'allumettes à retirer entre 1 et 6: ")
      if matches_removed in num_list:
        if int(matches_removed) <= nb_matches:
          nb_matches -= int(matches_removed)
        else:
          print(f"Il n'est pas possible de retirer plus d'allumettes que le nombre restant {player_2}.")
          continue
      else:
        print("Veuillez choisir un entier entre 1 et 6")
        continue
      if nb_matches == 0:
        print(f"Bravo {player_2}, vous avez retiré la dernière allumette !")
        break
    

matches_game_multi()