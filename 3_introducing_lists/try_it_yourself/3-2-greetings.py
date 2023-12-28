# Greetings: Start with the list you used in Exercise 3-1, but instead of just printing each person’s name, print a message to them. The text of each message should be the same, but each message should be personalized with the person’s name.

names = ["julia", "alex", "godi", "felix", "baingana", "julie"]

message = "please send all correspondence to millia@cook.com. Thank you."

print(f"Dear {names[0].title()}, {message}")
print(f"Dear {names[1].title()}, {message}")
print(f"Dear {names[2].title()} {message}")
print(f"Dear {names[3].title()}, {message}")
print(f"Dear {names[4].title()}, {message}")
print(f"Dear {names[5].upper()}, {message}")