#!/bin/bash

#####
# Ce script est destiné aux postes de travail sous Ubuntu

#####
# On nettoie le profil par défault
if (sudo userdel -r Utilisateur -f)
	then echo -e "L'utilisateur et ses données ont été supprimées."
else
	echo -e "Echec lors de la supression de l'utilisateur ou celui-ci n'existe plus."
fi

#####
# Mise à jour du système
if (sudo apt-get update -y)
	then echo -e "Le système a été mis à jour."
else
	echo -e "Echec lors de la mise à jour."
fi

#####
# Creation d'un nom d'hôte aléatoire grâce à la variable $RANDOM et attribution de celui-ci
hostname="PC$RANDOM"
if (sudo hostnamectl set-hostname $hostname);
	then echo -e "Le nom du pc est désormais : "$hostname 
else 
	echo -e "Problème avec le changement de nom d'hôte."
fi

#####
# Création de l'utilisateur déterminé, création de ses droits à son dossier home
# [ sudo useradd Utilisateur -d /home/Utilisateur ] &&
#"[ echo -e "Utilisateur:projet6" | sudo chpasswd ]
useradd -p $(openssl  passwd -crypt projet6) -m Utilisateur
	then echo -e "L'utilisateur et ses droits ont été créés."
else 
	echo -e "Erreur lors de la création de l'utilisateur."
fi

#####
# Création d'un utilisateur admin, création de ses droits à son dossier home

#if [ sudo useradd P6_Admin -d /home/P6_Admin ] &&
#[ echo -e "P6_Admin:projet6" | sudo chpasswd ]
if [ useradd -p $(openssl  passwd -crypt projet6) -m P6_Admin ]
	then echo -e "L'utilisateur Admin et ses droits ont été créés."
else 
	echo -e "Erreur lors de la création de l'utilisateur Admin ."
fi

# Changement du mot de passe par défaut du compte par défaut "support" et ajout des droits administrateurs
if (sudo usermod -aG sudo P6_Admin)
	then echo -e "Ajout des droits administrateur effectués sur P6_Admin."
else
	echo -e "Problème lors du changement du mot de passe de l'utilisateur Admin."
fi


#####
# Installation du SSH
if (sudo apt-get install openssh-server -y)
	then echo -e "L'accès SSH a été configuré."
else
	echo -e "Le SSH n'a pas été installé."
fi

#####
# Modification des droits d'accès à ce fichier
if (sudo chmod 750 script_linux.sh)
	then echo -e "Changement des droits d'accès sur le script effectué."
else
	echo -e "Problème lors de l'attribution des droits sur le fichier script."
fi

