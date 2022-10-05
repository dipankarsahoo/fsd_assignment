from art import *
from getpass import getpass
from termcolor import colored

def get_input_user_password():
    user_name = input("Please enter your user_name:  ")
    password = getpass("Please enter your password: ")
    
    return (user_name, password)

def landing_menu():
    print("Enter from below options to proceed:")
    print("1. Registration")
    print("2. Login(if user is already registered)")
    print("3. Exit")
    print()
    option = input()
    return int(option)

def welcome_message():
    tprint("Welcome    to      Phone book" )
    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
    
def user_menu():
    print()
    print(colored("------------------------------------------------------------------------------------------------" , 'green'))
    print("What do you want to do?")
    print("[view -a]    to view all saved contacts")
    print("[view]       to view a specific contact")
    print("[add]        to add a new contact")
    print("[update]     to update an existing contact")
    print("[del]        to delete a contact")
    print("[del -a]     to delete all contacts")
    print("[exit]       to exit the program")
    print()
    return input()
        
def are_you_registered():
    print()
    print(colored("Are you a registered user? [y/n]" , 'yellow'))
    print("To exit enter exit.")
    print()
    return input()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'