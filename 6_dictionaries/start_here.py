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
    "Tomas": "Rust",
    "Johannes": "JavaScript",
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


# ⭐⭐LOOPING THROUGH A DICTIONARY

# Several different ways exist to loop through dictionaries. You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

	# ⭐Looping through all key value pairs:

# The following dictionary would store one person’s username, first name, and last name:
user_0 = {
	"username": "hermit#2",
	"first_name": "mukulembeze",
	"last_name": "wilfred",
	}

# You can access any single piece of information about user_0 based on what you’ve already learned in this chapter. But what if you wanted to see everything stored in this user’s dictionary? To do so, you could loop through the dictionary using a for loop:

for key, value in user_0.items():
	print(f"\nKey: {key}")
	print(f"\nValue: {value.title()}")
	print('_______________________\n')

# To write a for loop for a dictionary, you create names for the two variables that will hold the key and value in each key-value pair. You can choose any names you want for these two variables. This code would work just as well if you had used abbreviations for the variable names, like this: 
	# for k, v in user_0.items():

# The second half of the for statement includes the name of the dictionary followed by the method items(), which returns a sequence of key-value pairs. The for loop then assigns each of these pairs to the two variables provided.

# In the preceding example, we use the variables to print each key, followed by the associated value. 


for name, language in favorite_languages.items():
    print(f"\nName: {name.title()}")
    print(f"language: {language}")
    print('************************\n')

# In this example, because the keys always refer to a person’s name and the value is always a language, we use the variables name and language in the loop instead of key and value. This makes it easier to follow what’s happening inside the loop:

for name, language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite programming language is {language.title()}")
print('__________________________________________________\n')

# The above code tells Python to loop through each key-value pair in the dictionary. As it works through each pair the key is assigned to the variable name, and the value is assigned to the variable language. These descriptive names make it much easier to see what the print() call is doing.

	# ⭐looping through all the keys in the dictionary - keys()
# This for loop below tells Python to pull all the keys from the dictionary favorite _languages and assign them one at a time to the variable name. The output shows the names of everyone who has a favorite language:

for name in favorite_languages.keys():
    print(name.title())
print('__________________________________________________\n')

# The keys() method is useful when you don’t need to work with all of the val- ues in a dictionary. Above we loop through favorite_languages and print the names of everyone who has a favorite language.

# Looping through the keys is actually the default behavior when looping through a dictionary, so this code would have exactly the same output if you wrote:	for name in favorite_languages:
# You can choose to use the keys() method explicitly if it makes your code easier to read, or you can omit it if you wish.

# You can access the value associated with any key you care about inside the loop, by using the current key. Let’s print a message to a couple of friends about the languages they chose. We’ll loop through the names in the dictionary as we did previously, but when the name matches one of our friends, we’ll display a message about their favorite language:

friends = ['Amy', 'Julia']

for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")
    
    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you work in {language.title()}.")

print('__________________________________________________\n')
#First, we make a list of friends that we want to print a message to. Inside the loop, we print each person’s name. Then we check whether the name we’re working with is in the list friends 1. If it is, we determine the person’s favorite language using the name of the dictionary and the current value of name as the key 2. We then print a special greeting, including a reference to their language of choice. Everyone’s name is printed, but our friends receive a special message:

# You can also use the keys() method to find out if a particular person was polled. This time, let’s find out if Keren took provided her language:

if 'Keren' not in favorite_languages.keys():
    print("Keren please tell us your preferred language, thanks!")
print('__________________________________________________\n')

# The keys() method isn’t just for looping: it actually returns a sequence of all the keys, and the if statement simply checks if 'Keren' is in this sequence. Because she’s not, a message is printed inviting her to tell us her language:

	#	⭐Looping Through a Dictionary’s Keys in a Particular Order

for name in sorted(favorite_languages.keys()):
    print(f"Hello {name}, thank you for letting us know.")
print('__________________________________________________\n')


# This for statement is like other for statements, except that we’ve wrapped the sorted() function around the dictionary.keys() method. This tells Python to get all the keys in the dictionary and sort them before starting the loop.

	# ⭐Looping Through All Values in a Dictionary - values()
# you can use the values() method to return a sequence of values without any keys.

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
print('__________________________________________________\n')

# The for statement here pulls each value from the dictionary and assigns it to the variable language. When these values are printed, we get a list of all chosen languages. 
# This approach pulls all the values from the dictionary without check- ing for repeats.
# To see each language chosen without repetition, we can use a set. A set is a collection in which each item must be unique.

print("Here is the list of all values without repetitions.")
for language in set(favorite_languages.values()):
    print(language.title())
print('__________________________________________________\n')

print("Here is the list of all values without repetitions and sorted in order.")
for language in sorted(set(favorite_languages.values())):
    print(language.title())
print('__________________________________________________\n')

# When you wrap set() around a collection of values that contains duplicate items, Python identifies the unique items in the collection and builds a set from those items. Here we use set() to pull out the unique languages in favorite_languages.values(). The result is a non-repetitive list of languages that have been mentioned.

	# Building or creating a set
# You can build a set directly using braces and separating the elements with commas:
cats = {'tiger', 'lion', 'leopard', 'jaguar', 'cheater'}

print(cats)

# It’s easy to mistake sets for dictionaries because they’re both wrapped in braces. When you see braces but no key-value pairs, you’re probably looking at a set.