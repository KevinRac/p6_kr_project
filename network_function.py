
#Fonction pour scan le réseau (IP)
def scan_network_utility():

    #Importation des dépendances
    import subprocess 
    import netifaces as ni
    import socket

    #Creation du socket + utilisation du dns de google pour determiner mon ip et on la récupère dans une variable 
    monip = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    monip.connect(("8.8.8.8", 80))
    monip = monip.getsockname()[0]

    #Affichage de l'IP
    print("Votre ip est :")
    print(monip)

    #On demande quel réseau analyser
    network_to_scan = input("Quel réseau voulez vous analyser ? Saisir les 3 premiers octets uniquement : ")

    #On fait un try pour vérifier le bon fonctionnement
    try:

        #On récupère la variable saisie, on y ajoute un "." + segment 1 à 254 et on essaye chaque combinaison entre 1 et 254
        for ping in range(1,254): 
            address = network_to_scan + "." + str(ping) 
            res = subprocess.call(['ping', '-c', '3', address])

            #Si la fonction trouve une IP, on l'affiche
            if res == 0: 
                print( "IP trouvée : ", address)

    #Si on presse Ctrl - C pour couper la fonctio nen cours, on affiche un message d'erreur       
    except KeyboardInterrupt: 
            print("\n Programme interrompu!") 
            sys.exit() 

#Fonction pour scan les ports d'une IP
def scan_ports_utility():

    #Importation des dépendances
    import subprocess
    import sys
    import socket
    from datetime import datetime 

    #On demande l'adresse ip à scanner
    ip_to_check=input("Veuillez saisir l'adresse IP à scanner : ")
    
    # Bannière affichant l'IP à scanner + la date/heure
    print("-" * 50) 
    print("Cible à scanner: " + ip_to_check) 
    print("Le scan à commencé le :" + str(datetime.now())) 
    print("-" * 50) 

    #On fait un try pour vérifier le bon fonctionnement 
    try: 
          
        # On scan les ports de 1 à 65536
        for port in range(1,65535): 
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
            sys.exit() 


#Fonction pour établir une connexion ssh
def connexion_ssh_utility():

    #Importation des dépendances
    import paramiko

    #On récupère les informations necessaires pour la connexion SSH
    ip=input("Veuillez saisir l'IP à laquelle se connecter : ")
    user=input("Veuillez saisir le nom d'utilisateur : ")
    passwd=input("Veuillez saisir le mot de passe : ")

    #initialisation de la connexion
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    #Si le client se connecte avec les paramètres, on initilise la connexion et on affiche que la connexion est établie
    if (client.connect(hostname=ip, username=user, password=passwd, timeout=4)) == 0:
        print("Connexion établie")

    #Sinon on affiche un message d'erreur
    else:
        print("Echec de la connexion")
        

#Fonction pour installer et ouvrir Wireshark
def wireshark_utility():

    #Importation des dépendances
    import os

    #On demande le mot de passe SuperUser
    os.system("apt-get install -y wireshark >sortie.log") ###miss
    os.system("wireshark") ###miss


#Fonction pour ping une IP
def ping_utility():

    #Importation des dépendances
    import os

    #On demande l'ip à ping
    ip_to_check=input("Veuillez saisir l'adresse IP à ping : ")

    #On initialise le ping dans une variable
    response = os.system("ping -c 1 " + ip_to_check)

    #Si cette variable renvoi 0 (pour ok) on affiche un message de succès
    if response == 0:
        pingstatus = "Ping OK"

    #Sinon on affiche une erreur de ping
    else:
        pingstatus = "Pas de ping"

    print("-" * 50) 
    print (pingstatus)
    print("-" * 50)
    
