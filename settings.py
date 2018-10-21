# Auteurs: Benjamin BEYERLE - Philippe DA SILVA OLIVEIRA
# Classe: SRC1 - 3E

# Ce fichier recense toutes les lib necessaire et déclare les variables globales, on as juste à importe settings
# dans les autres fichier pour utiliser les fonctions voulues
import sys
import string
import random
import csv
import hashlib
from getpass import getpass
import authenticate
import menu
import add
import delete
import list
import update
import string
import random


def init():

    global CSV_FILE
    CSV_FILE = './ressources/user.csv'
