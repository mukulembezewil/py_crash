#5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is not empty. 

# If the list is empty, print the message We need to find some users! 

# Remove all of the usernames from your list, and make sure the correct mes- sage is printed.

usernames = []

if usernames:
	for user in usernames:
		if user == 'admin':
			print(f'Hello {user}. Would you like to see a status report?')
		else:
			print(f"Welcome {user.title()}. Asante for logging in again.")
else:
    print('About time we found some users, isn\'t it?')