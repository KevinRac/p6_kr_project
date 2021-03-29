import os

def launch_script():

    user = input("Veuillez saisir le nom d'utilisateur à créer : ")
    os.system("sudo ./script_linux.sh >sortie.log")
     
    fichier = open('sortie.log', 'r')
    sortie = fichier.read()
    fichier.close()
     
    print (sortie)

def script_linux():

    if os.uname()[0] == 'Linux':
        launch_script()

    else:
        print ("Ce n'est pas le bon système d'exploitation")
