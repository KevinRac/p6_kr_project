#Importation des dépendances
import os
import display_menu

#Fonction pour lancer le script .sh
def script_linux():

    #On affiche ce que le script va faire
    print(" ------------------------------")
    print("Ce script permet de : ")
    print(" - réinitialiser le profil Utilisateur,")
    print(" - mettre à jour le système,")
    print(" - installer le paquet SSH,")
    print(" - créér l'utilisateur Admin",)
    print(" - regénèrer le nom d'hôte")
    print(" ------------------------------")

    #On demande à l'utilisateur de confirmer son choix
    confirm=input("Ce script supprimera le profil utilisateur et ses données, veuillez confirmer par o (oui) ou par n (non) : ")

    #Si son choix est "o" pour oui:
    if confirm == "o":

        #On affiche un message d'attente, on execute le script et on stock sa sortie (réponse du système) dans un fichier sortie.log
        print("Veuillez patienter, la commande s'exécute...")
        os.system("sudo ./script_linux.sh >sortie.log")

        #On stock le nom du fichier dans une variable, son contenu dans une autre et on affiche tout ce qui est écrit
        fichier = open('sortie.log', 'r')
        sortie = fichier.read()
        fichier.close()
        print (sortie)

        #On affiche le menu principal à la fin de la fonction
        display_menu.menu()

    #Si son choix est "n" pour non:
    elif confirm =="n":

        #On affiche un message d'avertissement et redirige vers le menu principal
        print ("Opération abandonnée")
        display_menu.menu()

    #Sinon on avertit l'utilisateur que le choix n'est pas défini, et on affiche à nouveau le début du script
    else:
        print ("Choix non défini")
        script_linux()
