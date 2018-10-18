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


def init():

    global CSV_FILE
    CSV_FILE = 'C:/Users/Benjamin/PycharmProjects/Projet1/ressources/user.csv'
