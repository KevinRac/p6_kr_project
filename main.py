# Importation des dépendances
from display_menu import *
from login_function import *


################################################################################    
############################ DEBUT DU PROGRAMME ################################
################################################################################

# Affichage du message de bienvenue  
print("           Bienvenue dans le script d'automatisation des tâches \n")

# Vérification, via la fonction login(), si le mot de passe saisie est le bon, puis on appelle la fonction permettant de gerer le menu
if login() == 0:
        menu()

