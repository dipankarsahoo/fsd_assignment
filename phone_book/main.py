

import display
import login_existing_user
import register
import read_all_contact
import read_one_contact
import add_new_contact
import update_contact
import delete_contact
import delete_all_contact
from termcolor import colored



color = display.bcolors()

while True:
    display.welcome_message()

    is_user_registered = display.are_you_registered()

    if is_user_registered.lower() == 'y':
        user_name , password = login_existing_user.get_user_input()
        if login_existing_user.verify_user(user_name, password):
            break
        else:
            continue

    elif is_user_registered.lower() == 'n':
        user_name , password = register.get_user_input()
        if register.verify_if_user_exists(user_name):
            continue
        else:
            register.add_new_user(user_name, password)
            continue
        
    elif is_user_registered.lower() == 'exit':
        quit()
    else:
        print(colored("Incorrect input , please eneter y or n.", 'red'))
        continue
    
    
while True:
    
    user_action = display.user_menu()
    
    match user_action:
        case 'view -a':
            read_all_contact.display_all_contacts(user_name)
            continue
        case 'view':
            read_one_contact.validate_and_search(user_name)
            continue
        case 'add':
            add_new_contact.insert_contact_info(user_name)
            continue
        case 'update':
            update_contact.update_contact(user_name)
            continue
        case 'del':
            delete_contact.delete_contact(user_name)
            continue
        case 'del -a':
            delete_all_contact.delete_all_contacts(user_name)
            continue
        case 'exit':
            quit()
        case default:
            print(colored("Please enter options from below menu to proceed/exit. " , 'red') )
            continue
            