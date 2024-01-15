# A Python dictionary is a data structure that stores a collection of Key-value pairs. Each key-value pair maps the key to its associated value. Dictionaries are created using curly braces and can be defined as objects with the data type 'dict'. They are ordered, changeable and do not allow duplicates. Dictionaries are commonly used to store and retrieve data based on a unique key.

# CREATING A DICTIONARY

alien_0 = {'color': 'green', 'points': 5, 'character': {'personality': 'sanguine', 'leadership': 'democratic'}}

# ACCESSING VALUES IN A DICTIONARY
# give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
print(alien_0['color'])
print(alien_0['points'])
print(alien_0['character']['leadership'])
print('_______________________\n')

new_points = alien_0['points']
print(f'You just hunted down {new_points}-points-worth of alien mass. Bro!')
print('_______________________\n')

# ADDING NEW KEY VALUE PAIRS

alien_0['x-position'] = 0
alien_0['y-position'] = 25

print(alien_0)
print('_______________________\n')

# STARTING WITH AN EMPTY DICTIONARY
alien_1 = {}

alien_1['color'] = 'pink'
alien_1['points'] = 10



print(alien_1)
print('_______________________\n')

# MODIFYING VALUES IN A DICTIONARY
# To modify a value in a dictionary, give the name of the dictionary with the key in square brackets and then the new value you want associated with that key.
alien_1['color'] = 'yellow'
print(alien_1)
print('_______________________\n')

alien_2 = {'x_position': 0, 'y_position': 20, 'speed': 'medium'}
print(f"Original position: {alien_2['x_position']}")

	# move the alien to the right.
	# determine how far to move the alien based on its current speed.

if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien.
    x_increment = 3

# the new position is the old position plus the increment
alien_2['x_position'] = alien_2['x_position'] + x_increment

print(f"New position: {alien_2['x_position']}")
print('_______________________\n')

# REMOVING KEY VALUE PAIRS - del

del alien_0['points']
print(alien_0)
print('_______________________\n')

# A DICTIONARY OF SIMILAR OBJECTS

favorite_languages = {
    "Jen": "C",
    "Phillip": "Java",
    "Antoine": "Rust",
    "Julia": "Julia",
    "Wil": "JavaScript",
    "Amy": "Go",
    }

print(favorite_languages)
print('_______________________\n')

print (f"Wil's favorite language is: {favorite_languages['Wil']}")
print('_______________________\n')

language = favorite_languages["Julia"]
print(f"Julia writs much of her code in {language}")
# We use this syntax to pull Julia's favorite language from the dictionary and assign it to the variable 'language'. Creating a new variable here makes for a much cleaner print() call than that for Wil above.
print('_______________________\n')

# USING get() TO ACCESS VALUES
# The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

print(favorite_languages.get("Jim", "The respondent was not polled."))
print(favorite_languages.get("Antoine"))

# If there’s a chance the key you’re asking for might not exist, consider using the get() method instead of the square bracket notation.

# If you leave out the second argument in the call to get() and the key doesn’t exist, Python will return the value None. The special value None means “no value exists.” This is not an error: it’s a special value meant to indicate the absence of a value. You’ll see more uses for None in Chapter 8.
print('_______________________\n')
