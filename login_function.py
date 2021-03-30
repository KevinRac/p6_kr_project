#Mot de passe par default
password_true="projet6"

#Importation des dépendances
import os


#Fonction de connexion
def login():

    #Si le système d'exploitation est "linux" (posix) :
    if os.name == 'posix':
        
        #Initialisation d'une variable à 1 (non ok)
        r=1

        #Tant que R (mot de passe)
        while r:

            #On demande de saisir le mot de passe et on le stock dans une variable
            welcome_pass=input("Veuillez saisir le mot de passe : ")

            #Si la variable contenant le mot de passe est égal à la variable du mot de passe défini, on retourne 0 pour ok
            if  welcome_pass == password_true:
                r=0
            #Sinon on retourne 1 pour non ok 
            else:
                r=1
                
        #On retourne la valeur et on continue la boucle tant qu'elle n'est pas ok
        return r

    #Sinon on affiche un message pour avertir que le système d'exploitation n'est pas supporté par le programme
    else:
        print ("Vous ne pouvez pas utiliser cet utilitaire sur ce système d'exploitation")

    
