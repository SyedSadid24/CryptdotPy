# version 1.11.25
# Importing modules...

import pyAesCrypt as cr
from termcolor import colored
from datetime import datetime as dt
import time
import argparse
import os, sys
import re

os.system('cls')

parser = argparse.ArgumentParser()
parser.add_argument('--mode', dest='mode', type=str, help='Encryption or Decryption')
parser.add_argument('--verbose', dest='verbose', type=str, help='Verbose mode')
#parser.add_argument('--filetype', dest='filetype', type=str, help='Types of various files') will be used in future version
args = parser.parse_args()

buffer_size = 64 * 1024 # Asigning buffer size

# Functions 

def name_change(name): # Function for changinf files name
    cname = re.findall('(.+).aes',name)
    str1 = ""   
    for ele in cname:  
        str1 += ele   
    return str1

def verbose_func():
    print("\nStarted Syncing files...\n")
    time.sleep(2)
    for fl in os.listdir():
        if fl == 'main.py':
            print(f"File found :  {fl} "+colored("[Not for encryption or decryption]","red"))
            #print(colored(f"File found : {fl} [Not for encryption or decryption.]","red"))
        else:
            print("File found : ",fl)
    print("\nScaned all files.")
    time.sleep(2)

# Encryption Decryption without verbose mode

if args.mode == 'encrypt' and args.verbose != 'on':

    password = input('\nEnter password : ')

    for files in os.listdir():
        if files == 'main.py':
            None
        else:
            cr.encryptFile(files,files+".aes",password,buffer_size)
            os.remove(files)

    print("\nFiles encryption done.")

elif args.mode == 'decrypt' and args.verbose != 'on':

    password = input('\nEnter password : ')

    for files in os.listdir():
        if files == 'main.py':
            None
        else:
            lname = name_change(files)
            cr.decryptFile(files,lname,password,buffer_size)
            os.remove(files)

    print("\nFiles decryption done.")

# Encryption Decryption with verbose mode

elif args.mode == 'encrypt' and args.verbose == 'on':

    password = input('\nEnter password : ')

    verbose_func()
    print("\nEncryption started\n")

    for files in os.listdir():
        if files == 'main.py':
            None
        else:
            cr.encryptFile(files,files+".aes",password,buffer_size)
            print(colored("Succesfully encrypted ","green")+": "+files)
            os.remove(files)
    print("\nFiles encryption done.")

elif args.mode == 'decrypt' and args.verbose == 'on':

    password = input('\nEnter password : ')

    verbose_func()
    print("\nDecryption started\n")

    for files in os.listdir():
        if files == 'main.py':
            None
        else:
            lname = name_change(files)
            cr.decryptFile(files,lname,password,buffer_size)
            print(colored("Succesfully decrypted ","green")+": "+files)
            os.remove(files)
    print("\nFiles decryption done.")

else:
    print("\ncommand whong!!")