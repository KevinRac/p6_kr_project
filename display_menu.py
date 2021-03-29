# Importation des fonctions
from display_menu import *
from login_function import *
from network_function import *
from script_function import *

#Fonction permettant de gérer les différents menus
def menu():

    #Variable contenant le choix du 1er menu
    choix = display_menu()

    # Si l'utilisateur saisit 1, on affiche le menu "réseau"
    if int(choix) == 1:

        #Variable contenant le choix du menu
        choix_reseau = display_menu_reseau()

        # Si l'utilisateur saisit 1, on lance la fonction scan_network_utility()
        if int(choix_reseau) == 1:
            scan_network_utility()

        # Si l'utilisateur saisit 2, on lance la fonction scan_ports_utility()   
        elif int(choix_reseau) == 2:
            scan_ports_utility()

        # Si l'utilisateur saisit 3, on lance la fonction connexion_ssh_utility()   
        elif int(choix_reseau) == 3:
            connexion_ssh_utility()

        # Si l'utilisateur saisit 4, on lance la fonction wireshark_utility()  
        elif int(choix_reseau) == 4:
            wireshark_utility()

        # Si l'utilisateur saisit 5, on lance la fonction ping_utility()
        elif int(choix_reseau) == 5:
            ping_utility()
            
        # Si l'utilisateur saisit 9, on revient au menu "réseau"
        elif int(choix_reseau) == 9:
            menu()

        # Si l'utilisateur saisit un nombre non défini, on renvoi un message d'avertissement
        else:
            print("Choix non défini")

    #Si l'utilisateur saisit 2, on affiche le menu "script de deploiement"   
    elif int(choix) == 2:
        display_menu_script()

        #Variable contenant le choix du menu
        choix_script = display_menu_script()

        # Si l'utilisateur saisit 1, on lance la fonction script_linux()
        if int(choix_script) == 1:
            script_linux()

        # Si l'utilisateur saisit 2, on lance la fonction script_windows()   
        elif int(choix_script) == 2:
            script_windows()

        # Si l'utilisateur saisit 9, on revient au menu "script de deploiement"    
        elif int(choix_script) == 9:
            menu()

        # Si l'utilisateur saisit un nombre non défini, on renvoi un message d'avertissement
        else:
            print("Choix non défini")
            
    # Si l'utilisateur saisit un nombre non défini dans le menu principal, on renvoi un message d'avertissement      
    else:
            print("Choix non défini")


#Fonction d'affichage du 1er menu après le login
def display_menu():
    
    print("1 - Reseau")
    print("2 - Script de déploiement")
    print("9 - Quitter")
    
    saisie_menu=input("Merci de saisir la fonction voulue en saisissant le chiffre : ")
    return saisie_menu

#Fonction d'affichage du menu "réseau"
def display_menu_reseau():
    
    print("1 - Utilitaire de scan réseau")
    print("2 - Utilitaire de scan des ports")
    print("3 - Connexion SSH")
    print("4 - Wireshark")
    print("5 - Ping")
    print("9 - Retour")
    
    saisie_menu_reseau=input("Veuillez selectionner l'utilitaire voulu en saisissant le chiffre : ")
    return saisie_menu_reseau

#Fonction d'affichage du menu "script de deploiement"
def display_menu_script():

    print("1 - Script d'installation Linux")
    print("2 - Script d'installation Windows")
    print("9 - Retour")
    
    saisie_menu_script=input("Veuillez selectionner l'utilitaire voulu en saisissant le chiffre : ")
    return saisie_menu_script
