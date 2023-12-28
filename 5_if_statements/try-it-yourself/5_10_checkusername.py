# 5-10. Checking Usernames: Do the following to create a program that simulates how websites ensure that everyone has a unique username. 

# Make a list of five or more usernames called current_users. 

# Make another list of five usernames called new_users. Make sure one or two of the new usernames are also in the current_users list. 

# Loop through the new_users list to see if each new username has already been used. If it has, print a message that the person will need to enter a new username. If a username has not been used, print a message saying that the username is available. 

# Make sure your comparison is case insensitive. If 'John' has been used, 'JOHN' should not be accepted. (To do this, you’ll need to make a copy of current_users containing the lowercase versions of all existing users.)

current_users = ["Joe2001", "Floydb", "Friesfrench", "UGAMOND"]
new_users = ["crimson", "clover", "might", "spirit", "yonatan", "floydb", "UGAMOND"]

# Below I use list comprehension to actually create copies of the two lists.
current_users_copy = [user.lower() for user in current_users]
new_users_copy = [user.lower() for user in new_users]

for new_user in new_users_copy:
    if new_user in current_users_copy:
        print(f"Sorry the user name {new_user} has already been used. Please enter a new user name.")
    else: 
        print(f"{new_user} is available.")