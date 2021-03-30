# Importation des dépendances
from network_function import *
from script_function import *

#Fonction permettant de gérer les différents menus
def menu():

    #Variable contenant le choix du 1er menu
    choix = display_menu()

    # Si l'utilisateur saisit 1, on affiche le sous-menu "réseau" via display_menu_reseau()
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

        # Si l'utilisateur saisit 4, on lance la fonction ping_utility()
        elif int(choix_reseau) == 4:
            ping_utility()
            
        # Si l'utilisateur saisit 9, on revient au menu principal
        elif int(choix_reseau) == 9:
            menu()

        # Si l'utilisateur saisit un choix non défini, on renvoi un message d'avertissement et on le renvoi au menu
        else:
            print("Choix non défini")
            menu()

    #Si l'utilisateur saisit 2, on lance le script de deploiement linux via la fonction script_linux() 
    elif int(choix) == 2:
        script_linux()
            
    # Si l'utilisateur saisit un nombre non défini dans le menu principal, on renvoi un message d'avertissement et on affiche à nouveau le menu     
    else:
        print("Choix non défini")
        menu()


#Fonction d'affichage du menu principal après le login
def display_menu():

    #On affiche les différents choix possibles
    print("---------------")
    print("1 - Reseau")
    print("2 - Script de déploiement")
    print("9 - Quitter")
    print("            ")

    #On demande le choix de l'utilisateur et on le stocke dans une variable qui va être retournée à la fonction menu()
    saisie_menu=input("Merci de saisir votre choix en saisissant le chiffre situé devant la fonction : ")
    return saisie_menu

#Fonction d'affichage du sous-menu "réseau"
def display_menu_reseau():

    #On affiche les différents choix possibles
    print("---------------")
    print("1 - Utilitaire de scan réseau")
    print("2 - Utilitaire de scan des ports")
    print("3 - Connexion SSH")
    print("4 - Ping")
    print("9 - Retour")
    print("            ")

    #On demande le choix de l'utilisateur et on le stocke dans une variable qui va être retournée à la fonction menu()
    saisie_menu_reseau=input("Veuillez selectionner l'utilitaire voulu en saisissant le chiffre : ")
    return saisie_menu_reseau
