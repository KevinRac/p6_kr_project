****************************************
  Script d'automatisation des taches  
****************************************


***********Prérequis**************

  - OS : Linux
  - Installer Python3

**********Fonctionnement**********

 - Copier l'ensemble des fichiers dans un dossier de l'ordinateur
 - Executer le fichier main.py en effectuant un "python3 main.py" depuis un interpreteur de commande
 - Le mot de passe demandé est noté dans les fichiers. Celui-ci à pour but de proteger le programme contre d'eventuels utilisateurs non informés ayant trouvé ce programme.

**********Utilitaires*************

Ce script Python permet de :

 - (choix dans le menu)   Description                                          ->   [entrée]                                                      [sortie]

 - (choix 1 puis 1)       Scanner le réseau sur le lequel le PC est connecté   ->   []                                                            [Indique les adresses IP renvoyant un ping ok]
 - (choix 1 puis 2)       Scanner les ports d'une adresse IP spécifiée         ->   [Saisir l'adresse IP du PC à scanner]                         [Indique les ports ouverts]
 - (choix 1 puis 3)       Lancer un terminal avec une connexion ssh            ->   [Saisir l'adresse IP et le nom d'utilisateur du PC distant]   [Ouvre un terminal et demande le mot de passe du PC distant]
 - (choix 1 puis 4)       Effectuer un ping vers une adresse IP spécifiée      ->   [Saisir l'adresse IP du PC à ping]                            [Indique l'état du ping]

 - (choix 2 puis 1)       Lancer un script d'installation de PC Client Linux   ->   [Demande de confirmation]                                     [Execution du script et renvoi les commandes effectuées]

***********Notes DEV************

 - Chaque ligne de code est commentée pour comprendre son fonctionnement
