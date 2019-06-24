import json, os, re

def get_valid_alphanumeric_input(prompt_string):
	response = input(prompt_string)
	while not re.match(r'^([a-zA-Z0-9_\-\(\)])+$', response):
		print("Invalid input, please use only alphanumeric characters undescores dashes or parentheses.")
		response = input(prompt_string)
	return response


def get_valid_numeric_input(prompt_string):
	response = input(prompt_string)
	while not re.match(r'^([0-9])+$', response):
		print("Invalid input, please use only numeric characters.")
		response = input(prompt_string)
	return response

def edit_generic_level_identifiers(current_config, type):
	backup_config = current_config
	if type not in current_config['iSense_info']['field_identifiers']:
		current_config['iSense_info']['field_identifiers'][type] = {}
	option_dictionary = {'1':'Cancel', '2':'Save and return to previous menu', '3': 'Create new node identifier', '4': 'Edit existing node identifier',
	'5': 'Delete existing node identifier'}
	print("What do you want to do?")
	print('-------------------------------------------------------------------')
	while True:
		for index in sorted(option_dictionary):
			print('{0}. {1}'.format(index, option_dictionary[index]))
		selection = input("Please enter the appropriate number to indicate your choice: ")
		if selection == '1':
			print('-------------------------------------------------------------------')
			print('Successfully canceled changed')
			return backup_config
		if selection == '2':
			print('-------------------------------------------------------------------')
			print('Successfully saved changes')
			return current_config
		if selection == '3':
			print('-------------------------------------------------------------------')
			field_name = get_valid_alphanumeric_input("Please enter the new "+ type + " field name: ")
			field_identifier = get_valid_numeric_input("Please enter the new "+ type + " field identifier: ")
			current_config['iSense_info']['field_identifiers'][type][field_name] = field_identifier
			print('Successfully added a new ' + type + ' identifier')
		if selection == '4':
			print('-------------------------------------------------------------------')
		if selection == '5':
			print('-------------------------------------------------------------------')
			identifier_dictionary = {'1':'Cancel'}
			for indx, val in enumerate(current_config['iSense_info']['field_identifiers'][type].keys()):
				identifier_dictionary[str(indx + 2)] = val
			for indx in sorted(identifier_dictionary):
				print('{0}. {1}'.format(indx, identifier_dictionary[indx]))
			choice = get_valid_numeric_input("Which " + type + " identifier would you like to delete: ")
			if choice == '1':
				continue
			if choice in list(identifier_dictionary):
				ans_string = input('Are you sure you want to delete ' + identifier_dictionary[choice] + ' ? (Y/n): ')
				ans = ans_string[0].lower()
				if ans == 'y':
					print('-------------------------------------------------------------------')
					print('Successfully deleted ' + identifier_dictionary[choice])
					del current_config['iSense_info']['field_identifiers'][type][identifier_dictionary[choice]]
				else:
					print('-------------------------------------------------------------------')
					print('Delection canceled')

def edit_field_identifiers(current_config):
	backup_config = current_config
	if 'field_identifiers' not in current_config['iSense_info']:
		current_config['iSense_info']['field_identifiers'] = {}
	option_dictionary = {'1':'Cancel', '2' : 'Save and return to previous menu', '3': 'Edit timestamp identifier', '4' : 'Edit reading identifier',
	'5': 'Edit node level identifiers', '6': 'Edit sesor level identifiers'}
	print("What do you want to do?")
	print('-------------------------------------------------------------------')
	while True:
		for index in sorted(option_dictionary):
			print('{0}. {1}'.format(index, option_dictionary[index]))
		selection = input("Please enter the appropriate number to indicate your choice: ")
		if selection == '1':
			print('-------------------------------------------------------------------')
			print('Successfully canceled changes')
			return backup_config
		if selection == '2':
			print('-------------------------------------------------------------------')
			print('Successfully saved changes')
			return current_config
		if selection == '3':
			timestamp_identifier = get_valid_numeric_input("Please enter the timestamp identifier: ")
			current_config['iSense_info']['field_identifiers']['timestamp_identifier'] = timestamp_identifier
			print('-------------------------------------------------------------------')
			print('Successfully changed the timestamp identifier')
		if selection == '4':
			reading_identifier = get_valid_numeric_input("Please enter the reading identifier: ")
			current_config['iSense_info']['field_identifiers']['reading_identifier'] = reading_identifier
		if selection == '5':
			edit_generic_level_identifiers(current_config, 'node_level')
		if selection == '6':
			edit_generic_level_identifiers(current_config, 'sensor_level')
def edit_iSense_config(current_config):
	backup_config = current_config
	if 'iSense_info' not in current_config:
		current_config['iSense_info'] = {}
	option_dictionary = {'1':'Cancel', '2': 'Save and return to previous menu',  '3': 'Edit dataset ID', '4':'Edit contribution key', '5': 'Edit field identifiers'}
	print("What do you want to do?")
	print('-------------------------------------------------------------------')
	while True:
		for index in sorted(option_dictionary):
			print('{0}. {1}'.format(index, option_dictionary[index]))
		selection = input("Please enter the appropriate number to indicate your choice: ")
		if selection == '1':
			print('-------------------------------------------------------------------')
			print('Successfully canceled changes')
			return backup_config
		if selection == '2':
			print('-------------------------------------------------------------------')
			print('Successfully saved changes')
			return current_config
		if selection == '3':
			dataset_id =  get_valid_numeric_input("Please enter the iSense dataset ID: ")
			current_config['iSense_info']['dataset_id'] = dataset_id
			print('-------------------------------------------------------------------')
			print("Successfully changed the dataset ID")
		if selection == '4':
			contribution_key = get_valid_alphanumeric_input("Please enter the iSense contribution key: ")
			current_config['iSense_info']['contribuition_key'] = contribution_key
			print('-------------------------------------------------------------------')
			print("Successfully changed the contribution_key")
		if selection == '5':
			edit_field_identifiers(current_config)
test = {}
edit_iSense_config(test)
