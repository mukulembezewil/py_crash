# 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner. 

  # Start with your program from Exercise 3-4 or 3-5. Add a print() call to the end of your program, informing people that you found a bigger table. 
  # Use insert() to add one new guest to the beginning of your list. 
  # Use insert() to add one new guest to the middle of your list. 
  # Use append() to add one new guest to the end of your list.

invitees = ["Mrs. Mugume", "Dr. Emma", "Eng. Terry"]
print(f"{invitees[1]} will not make it.")
print("+++++++++++++++++++++++++++++++++++++++++")

invitation = "this is to cordially invite you to dinner this Thursday at 8:00pm at Ritz Carlton Boston rooftop restaurant. See you then. Wil"

print("Great people I found a larger table.")

invitees.insert(0, "Princess Carla")
invitees.insert(2, "Governor Oz")
invitees.append("Prof. Jackson")

print(f"Dear {invitees[0]} {invitation}")
print(f"Dear {invitees[1]} {invitation}")
print(f"Dear {invitees[2]} {invitation}")
print(f"Dear {invitees[3]} {invitation}")
print(f"Dear {invitees[5]} {invitation}")
print(f"Dear {invitees[4]} {invitation}")
