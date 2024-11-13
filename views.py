# les fonctions qui affichent
from consts import *
from functions import clean, pause, connexion, addClient,pret

def header(title,subtitle,motif):
    clean()
    print('-'*SCREEN)
    print(title.upper().center(SCREEN,motif))
    print("{:->60}".format(subtitle.upper()))

def page_connection():
    header(APP_NAME,'CONNEXION','~')
    login = input("Login     : ")
    mdp = input("Password  : ")
    #Verifier si l'utilisateur existe dans le fichier users
    return connexion(login,mdp)
    
def menu_general(user_name='MENU PRINCIPAL'):
    header(APP_NAME,user_name,'*')
    print("1. Nouveau Client")
    print("2. Faire un pret")
    print("3. Faire un remboursement")
    print("4. Quitter")
    choix = input("Faites votre choix : ")
    return choix

def new_client(connected_username):
    header(APP_NAME,connected_username,'~')
    print("-------------------")
    print("CREATION DE COMPTE:")
    print("-------------------")
    nom = input("Nom : ")
    prenom = input("Prenom : ")
    tel = input("Tel : ")
    if len(nom.strip()) > 0 and len(prenom.strip()) > 0 and len(tel.strip()) > 0:
        addClient(nom, prenom, tel)

def faire_un_pret(connected_username):
    header(APP_NAME,connected_username,'~')
    print("-------------------")
    print("FAIRE UN PRETE:")
    print("-------------------")
    tel = input("Tel : ")
    montant = int(input("Montant : "))
    if len(tel.strip()) > 0 and montant > 0:
        pret(tel, montant)

if __name__ == '__main__':
    header('TEST APP','Exemple','@')
    pause()
    menu_general()