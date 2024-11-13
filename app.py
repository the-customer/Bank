# le fichier principal
# import views
# views.page_connection()
# ----------------
# from views import (SCREEN as ecran, 
#                    page_connection as pc)
# SCREEN = 12
# print(SCREEN)
# print(ecran)
# pc()
# --------------
# from views import *
# page_connection()

from views import page_connection, menu_general,new_client,faire_un_pret
from functions import pause
connected_username = None



while True:
    connected_username = page_connection()
    if connected_username is not None:
        break
    
while True:
    choix = menu_general(connected_username)
    if choix == '1':
        new_client(connected_username)
    elif choix == '2':
        faire_un_pret(connected_username)
    elif choix == '3':
        print("Faire un remboursement")
    elif choix == '4':
        print("Quitter")
        break
    else:
        print("Choix invalide!")
        pause()