#!/bin/bash

#####
# Ce script est destiné aux postes de travail sous Ubuntu

#####
# On nettoie le profil par défault
if (sudo apt-get update && sudo apt-get install wireshark -y && sudo wireshark)
	then echo -e "Le programme a été executé."
else
	echo -e "Echec"
fi

