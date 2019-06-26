import json,os,re
PATH_TO_CONFIG_FOLDER = 'configuration/'
FILENAME_FOR_ACTIVE_CONFIG = 'active_configuration.txt'

def pick_config_or_cancel(prompt_string):
    list_of_configs = [file_name for file_name in os.listdir(PATH_TO_CONFIG_FOLDER) if not file_name == FILENAME_FOR_ACTIVE_CONFIG]
    print('-------------------------------------------------------------------')
    while True:
        print(prompt_string)
        print('1. Cancel')
        valid_choices = set()
        for index,name in enumerate(list_of_configs):
            valid_choices.add(str(index+2))
            print("{0}. {1}".format(index+2,name[:-5]))
        choice = input('Enter the number corresponding to your selection: ')
        if choice == '1': return 'Cancel'
        if choice in valid_choices: return list_of_configs[int(choice)-2]
        print('-------------------------------------------------------------------')
        print("Error, invalid input.")



def pick_subdict_or_cancel(subdict, prompt_string):
    list_of_keys = list(subdict.keys())
    valid_choices = set()
    for index,name in enumerate(list_of_keys):
        valid_choices.add(str(index+2))
    print('-------------------------------------------------------------------')
    while True:
        print(prompt_string)
        print('1. Cancel')
        for index,name in enumerate(list_of_keys):
            print("{0}. {1}".format(index+2,name))
        choice = input('Enter the number corresponding to your selection: ')
        if choice == '1': return 'Cancel'
        if choice in valid_choices: return list_of_keys[int(choice)-2]
        print('-------------------------------------------------------------------')
        print("Error, invalid input.")


#print(pick_subdict_or_cancel({1:True,2:False},"Which cuh do you want?"))

def get_confirmation(message):
    print(message)
    return 'y' == input('(Y/n): ')[0].lower()

def get_regex_input(regex, prompt_string, error_string):
	response = input (prompt_string)
	while not re.match(regex, response)
		print(error_string)
		response = input(prompt_string)
	return response

def editing_menu_with_backup(subdictionary,prompt_string,options_list):
    backup = json.loads(json.dumps(subdictionary))
    valid_choices = set()
    for index,name in enumerate(options_list):
        valid_choices.add(str(index+3))
    print('-------------------------------------------------------------------')
    while True:
        print(prompt_string)
        print('1. Cancel and return to previous menu')
        print('2. Save and return to previous menu')
        for index,value in enumerate(options_list):
            print('{0}. {1}'.format(index+3,value[0]))
        choice = input('Enter the number corresponding to your selection: ')
        if choice == '1': return backup
        if choice == '2': return subdictionary
        if choice in valid_choices:
            options_list[int(choice)-3][1](subdictionary)
            print('-------------------------------------------------------------------')
            continue
        print('-------------------------------------------------------------------')
        print('Error, invalid input')

#a = {1:True,2:False}
#a = editing_menu_with_backup(a,'Pick an option',[('Add 3-True',lambda x: x.update({3:True} or x)),('Toggle 1',lambda x: x.update({1:not x[1]} or x))])
#print(a)



def basic_selection_menu(prompt_string,options_list):
    valid_choices = set()
    for index,name in enumerate(options_list):
        valid_choices.add(str(index+2))
    print('-------------------------------------------------------------------')
    while True:
        print(prompt_string)
        print('1. Cancel')
        for index,value in enumerate(options_list):
            print('{0}. {1}'.format(index+2,value[0]))
        choice = input('Enter the number corresponding to your selection: ')
        if choice == '1': return
        if choice in valid_choices:
            print('-------------------------------------------------------------------')
            return options_list[int(choice)-2][1]
        print('-------------------------------------------------------------------')
        print('Error, invalid input')






#def new_configuration():print('-------------------------------------------------------------------');print('new')
def edit_configuration():print('-------------------------------------------------------------------');print('edit')
#def delete_configuration():print('-------------------------------------------------------------------');print('delete')
#def set_active():print('-------------------------------------------------------------------');print('active')

def new_configuration():
    print('-------------------------------------------------------------------')
    choice = basic_selection_menu('What would you like to do?',
                                  [('Create new empty configuration','empty'),
                                   ('Create copy of existing configuration','copy')])
    if choice == 'empty':
        name = get_regex_input(r'^([a-zA-Z0-9_\-\(\)])+$',
                               'What should the configuration be named',
                               'Error, name may only contain letters numbers underscores or parentheses')
        f = open(PATH_TO_CONFIG_FOLDER + name + '.json','w')
        f.write('{}')
        f.close()
        print('-------------------------------------------------------------------')
        print('Successfully added new configuration' + name)
        return
    if choice == 'copy':
        
        

def delete_configuration():
    print('-------------------------------------------------------------------')
    choice = pick_config_or_cancel('Which configuration do you want to delete?')
    if choice == 'Cancel':
        print('-------------------------------------------------------------------')
        return
    f = open(PATH_TO_CONFIG_FOLDER + FILENAME_FOR_ACTIVE_CONFIG, 'r')
    line = f.read()
    f.close()
    if line==choice:
        print('-------------------------------------------------------------------')
        print('Cannot delete active configuration. Deletion cancelled')
        return
    if get_confirmation('Are you sure you want to delete '+choice[:-5]+' forever?'):
        os.remove(PATH_TO_CONFIG_FOLDER+choice)
        print('-------------------------------------------------------------------')
        print('Successfully deleted '+choice[:-5])
    else:
        print('-------------------------------------------------------------------')
        print('Deletion cancelled')


def set_active():
    print('-------------------------------------------------------------------')
    choice = pick_config_or_cancel('Which configuration do you want to set active?')
    if choice == 'Cancel':
        print('-------------------------------------------------------------------')
        return
    f = open(PATH_TO_CONFIG_FOLDER + FILENAME_FOR_ACTIVE_CONFIG, 'w')
    f.write(choice)
    f.close()
    print('-------------------------------------------------------------------')
    print('Successfully set '+choice[:-5]+' as active configuration')


def main_menu():
    option_dictionary = {'1':'Cancel','2':'Add new configuration','3':'Edit configuration','4':'Delete configuration','5':'Set the active configuration'}
    print('-------------------------------------------------------------------')
    while True:
        print('What would you like to do?')
        for index in sorted(option_dictionary):
            print('{0}. {1}'.format(index, option_dictionary[index]))
        selection = input('Please enter the appropriate number to indicate your choice: ')
        if selection == '1':
            return
        if selection == '2':
            new_configuration()
            continue
        if selection == '3':
            edit_configuration()
            continue
        if selection == '4':
            delete_configuration()
            continue
        if selection == '5':
            set_active()
            continue
        print('-------------------------------------------------------------------')
        print('Invalid choice')

main_menu()