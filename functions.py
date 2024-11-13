# les fonction de traitement (logiques)
import os
import time
from genericpath import exists
from consts import FILE_USERS,FILE_CLIENT

def pause():
    input("Appuyez sur une touche pour continuer...")
def clean():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')
    # os.system('cls' if os.name=='nt' else 'clear')
def connexion(login, password):
    with open(FILE_USERS, 'r') as f:
        for user in f:
            # listeUser = user.strip().split(";")
            # nom = listeUser[0]
            # login = listeUser[1]
            # password = listeUser[2]
            nomUser, loginUser, passwordUser = user.strip().split(";")
            if loginUser == login and passwordUser == password:
                print("Connexion réussie!")
                return nomUser
        print("Login ou mot de passe invalide!!!")
        pause()
        return None
    
def addClient(nom,prenom,tel):
    with open(FILE_CLIENT, 'a') as f:
        f.write(f"{nom};{prenom};{tel}\n")
    print("Nouveau client créé avec succès!")
    pause()

def pret(tel,montant):
    with open(FILE_CLIENT, 'r') as f:
        for client in f:
            if len(client.strip()) > 1:
                nom,prenom,telClient = client.strip().split(";")
                if telClient == tel:
                    fichierClient = f"./data/loans/{tel}.txt"
                    # Tester si le client a au moins un pret : tester si le fichier avec son numero de telephone existe
                    if not exists(fichierClient):
                        with open(fichierClient, 'w') as f2:
                            f2.write(f"{montant};")
                            print(f"Le dossier est créé avec un pret de {montant} 💩!")
                            pause()
                    else:
                        with open(fichierClient, 'a') as f2:
                            pass
                    break
