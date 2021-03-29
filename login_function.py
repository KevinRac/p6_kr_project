#Mot de passe par default
password_true="projet6"

#Fonction de connexion
def login():

    #Initialisation d'une variable à 1 (non ok)
    r=1

    #Tant que R (mot de passe)
    while r:
        welcome_pass=input("Veuillez saisir le mot de passe : ")  
        if  welcome_pass == password_true:
            r=0
        else:
            r=1
    return r
