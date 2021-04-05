#!/usr/bin python3

#Importation des dépendances
import display_menu
import time
import subprocess 
import netifaces as ni
import socket
import sys
from datetime import datetime
import os

##########################################################################################################

#Fonction pour scan le réseau (IP)
def scan_network_utility():

    #Creation du socket + utilisation du dns de google pour determiner mon ip et on la récupère dans une variable 
    monip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    monip.connect(("8.8.8.8", 80))
    monip = monip.getsockname()[0]

    #On affiche l'IP du PC
    print("Votre ip est :")
    print(monip)
    print("         ")
    
    #On récupère les 3 premiers octets de l'adresse IP
    monipexplode= monip.split('.')[0]+"."+monip.split('.')[1]+"."+monip.split('.')[2]+"."


    #On fait un try pour vérifier le bon fonctionnement
    try:

        #On initialise une variable qui va passer de 1 à 254 à chaque saut
        for ping in range(1,254):

            #On défini la variable contenant les 3 premiers octets et on y incrémente la variable ping allant de 1 à 254
            address = monipexplode + str(ping)

            

            #On effectue le test avec la commande ping et on envoi la sortie vers NULL (supprime l'affichage des lignes de commandes)
            FNULL = open(os.devnull, 'w')
            res = subprocess.call(['ping', '-c', '3', address],stdout=FNULL, stderr=subprocess.STDOUT)

            #Si la fonction trouve une IP (0=ok), on l'affiche ainsi que son nom d'hôte
            if res == 0:
                
                print( "------------------------")
                print( "IP trouvée : ", address)
                hostname=os.popen('dig -x '+address+' +short')
                print( "Nom d'hôte : ", hostname.read())
                print( "        ")

    #Si on presse Ctrl - C pour couper la fonction en cours, on affiche un message d'erreur       
    except KeyboardInterrupt: 
            print("\n Programme interrompu!")

    #On affiche le menu à la fin de la fonction
    display_menu.menu()

##########################################################################################################

#Fonction pour scan les ports d'une adresse IP
def scan_ports_utility():

    #On demande l'adresse ip à scanner et l'initialise dans une variable
    ip_to_check=input("Veuillez saisir l'adresse IP à scanner : ")
    
    # Bannière affichant l'IP à scanner + la date/heure
    print("-" * 50) 
    print("Cible à scanner: " + ip_to_check) 
    print("Le scan à commencé le :" + str(datetime.now())) 
    print("-" * 50) 

    #On fait un try pour vérifier le bon fonctionnement 
    try: 
          
        # On initialise une variable qui va passer de 1 à 65536
        for port in range(1,65535):

            #Creation du socket de connexion
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            socket.setdefaulttimeout(1) 
              
            # On retourne le résultat si on trouve un port
            result = s.connect_ex((ip_to_check,port)) 
            if result ==0: 
                print("Le port {} est ouvert".format(port))
            s.close()
            
    #Si on presse Ctrl - C pour couper la fonctio nen cours, on affiche un message d'erreur       
    except KeyboardInterrupt: 
            print("\n Programme interrompu!")

    #On affiche le menu à la fin de la fonction
    display_menu.menu()

##########################################################################################################

#Fonction pour établir une connexion ssh
def connexion_ssh_utility():


    #On récupère les informations necessaires pour la connexion SSH
    ip=input("Veuillez saisir l'IP à laquelle se connecter : ")
    user=input("Veuillez saisir le nom d'utilisateur : ")

    #On affiche un message d'avertissement à l'utilisateur en mettant 3 seconde de délai
    print("Vous allez basculer vers le terminal, merci de saisir le mot de passe et de saisir vos commandes en ssh")
    print("Si le nouveau terminal ne s'ouvre pas après 3 secondes, l'identifiant ou l'adresse IP n'est pas correct")
    time.sleep(3)
    
    #On lance un terminal en ajoutant la commande ssh utilissateur@ip
    os.system("gnome-terminal -x ssh "+user+"@"+ip+"")

    #On affiche le menu à la fin de la fonction
    display_menu.menu()

##########################################################################################################

#Fonction pour ping une IP
def ping_utility():

    #On demande l'ip à ping
    ip_to_check=input("Veuillez saisir l'adresse IP à ping : ")

    #On initialise le ping dans une variable
    response = os.system("ping -c 1 " + ip_to_check)

    #Si cette variable renvoi 0 (ok), on stock "Ping ok" dans une variable
    if response == 0:
        pingstatus = "Ping OK"

    #Sinon on stock "Pas de ping" dans une variable
    else:
        pingstatus = "Pas de ping"

    #On affiche le resultat de la variable
    print("-" * 50) 
    print (pingstatus)
    print("-" * 50)

    #On met un delai de 3 secondes avant d'afficher le menu à la fin de la fonction
    time.sleep(3)
    display_menu.menu()
