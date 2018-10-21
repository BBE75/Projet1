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
