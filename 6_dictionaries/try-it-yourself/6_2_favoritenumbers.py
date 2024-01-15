# Favorite Numbers: Use a dictionary to store people’s favorite numbers. Think of five names, and use them as keys in your dictionary. Think of a favorite number for each person, and store each as a value in your dictionary. Print each person’s name and their favorite number.

fav_number = {
    "Mem": 12,
    "Hierophant": 6,
    "Fool": 0,
    }

for key in fav_number:
    print(f"{key}'s favorite number is {fav_number[key]}")