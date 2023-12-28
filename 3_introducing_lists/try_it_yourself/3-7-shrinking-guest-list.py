# 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and now you have space for only two guests.

# Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner. 
# Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner. 
# Print a message to each of the two people still on your list, letting them know they’re still invited. 
# Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

invitees = ["Mrs. Mugume", "Dr. Emma", "Eng. Terry"]
print(f"{invitees[1]} will not make it.")
print("+++++++++++++++++++++++++++++++++++++++++")

invitation = "this is to cordially invite you to dinner this Thursday at 8:00pm at Ritz Carlton Boston rooftop restaurant. See you then. Wil"

print("Great people I found a larger table.")

invitees.insert(0, "Princess Carla")
invitees.insert(2, "Governor Oz")
invitees.append("Prof. Jackson")

print(f"Dear {invitees[0]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print(f"Dear {invitees[1]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print(f"Dear {invitees[2]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print(f"Dear {invitees[3]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print(f"Dear {invitees[5]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print(f"Dear {invitees[4]} {invitation}")
print("+++++++++++++++++++++++++++++++++++++++++")

print("Haaa sorry folks. Things changed. Only two of you can come.")
print("+++++++++++++++++++++++++++++++++++++++++")

invitees.pop(5)
invitees.pop(4)
invitees.pop(3)
invitees.pop(2)

print("+++++++++++++++++++++++++++++++++++++++++")
print(invitees)

print("+++++++++++++++++++++++++++++++++++++++++")
print(f"Dear {invitees[0]} it appears you are one two blessed ones.")
print("++++++++++++++++++++++++++++++++++++++++++++")
print(f"Dear {invitees[1]}, it appears y'all blessed of all em.")

del invitees[1]
del invitees[0]

print("++++++++++++++++++++++++++++++++++++++++++++")
print(invitees)