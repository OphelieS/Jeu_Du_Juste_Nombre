from random import randint
import sys

banner = """
      _              _          ____         _
     | | _   _  ___ | |_  ___  |  _ \  _ __ (_)__  __
  _  | || | | |/ __|| __|/ _ \ | |_) || '__|| |\ \/ /
 | |_| || |_| |\__ \| |_|  __/ |  __/ | |   | | >  <
  \___/  \__,_||___/ \__|\___| |_|    |_|   |_|/_/\_\
                                            by Ophélie
        """

print(banner)

def play():
    mode = input("Choisis le mode du jeu jeu : \n - (H)ard (1000 nombre en 10) \n - (N)ormal (500 en 10) \n - (E)asy (100 en 10) \n - (Q)uit --->")
    dico = {"H": 1000, "N": 500, "E": 100}
    if mode in ["H", "N", "E", "h", "n", "e", "Q", "q"]:
        if mode == "Q" or mode == "q":
            sys.exit("Tu as quitté le jeu. Fait par Ophélie")
        max = dico.get(mode)
        number = generate(max)
        print(f"Le nombre est compris entre 0 et {max}")
        nb_tours = 0
        while nb_tours != 10:
            choice = int(input("Quel est ton nombre ? (seulement nombre) --> "))
            if choice > number:
                print("Le nombre est plus petit")
            elif choice < number:
                print("Le Nombre est plus grand")
            elif choice == number:
                bravo = f"Bravo tu as gagné en {nb_tours}, Si tu veux de nouveau essayer, tu peux lancer le programme à nouveau ! Bonne chance !"
                print(bravo)
                return 0
            nb_tours = nb_tours + 1
    else:
        print("*** Valeur incorrecte ***")
        play()

def generate(max):
    return randint(0, max)

if __name__ == "__main__":
    play()
