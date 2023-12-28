# WORKING WITH LISTS

	# LOOPING THROUGH AN ENTIRE LIST

book_list = ['genesis', 'numbers', 'exodus', 'leviticus']


for book in book_list: 
	print(book)

print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

tricksters = ["moses", "joshua", "samson", "jacob"]

for trickster in tricksters:
	print(f"Hey {trickster.title()} that was a heck of a trick you pulled there sir.")
	print(f"Folks are looking forward to your next show {trickster.title()}")
	print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print("Thanks folks. That was a terrific show.")

# You can write as many lines of code as you like in the for loop. Every indented line following the line for trickster in tricksters is considered inside the loop, and each indented line is executed once for each value in the list.
print("\n+-+-+-+-+-+-+-Generate a series of numbers+-+-+-+-+-+-\n")

	# MAKING NUMERICAL LISTS

		# Using the range() function - to generate a series of numbers.
for value in range(1, 5):
	print(value)
print("\n+-+-+-+-+-Pass range() only one argument-+-+-+-+-+-\n")

		# You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(7) would return the numbers from 0 through 6.
for value in range(7):
	print(value)
print("\n+-+-+-+-+-+-Create a List of numbers -+-+-+-+-+-+-+-+-\n")

    # Use range() with list() to create a 'List' of numbers
    # simply convert the results of range() directly into a list using the list() function. When you wrap list() around a call to the range() function, the output will be a "list" of numbers.
numbers = list(range(1, 6))
print(numbers)
print("\n+-+-+-+-+-+-Create list of even numbers +-+-+-+-+-+-+-+-+-\n")

    # Use range() to skip numbers in a given range - simply pass a third argument to range() which Python uses as a step size when generating numbers.
# e.g. to list the even numbers between 1 and 10
even_numbers = list(range(2, 11, 2))
print(even_numbers)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# Using range() You can create almost any set of number you want 
    # e.g. to make a list of the first 10 square numbers
square_numz = []
for value in range(1, 11):
	square = value ** 2
	square_numz.append(square)
print(square_numz)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")


# You could have written the above more concisely by omitting the temporary variable
square_numz = []

for value in range(1, 11):
	square_numz.append(value ** 2)
print(square_numz)  


# SIMPLE STATISTICS WITH A LIST OF NUMBERS

    # min() returns the minimum number in a list

print("\n Minimum Number is: +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
digits  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 15]
print(min(digits))

    # max() returns the maximum number in a list

print("\n Maximum Number is: +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
print(max(digits))

    # sum() returns the sum of all numbers in a list

print("\n Sum of Numbers is: +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
print(sum(digits))


# LIST COMPREHENSIONS
	# A list comprehension combines the "for loop" and the creation of new elements into one line, and automatically appends each new element.

print("\n Square numbers using list comprehensions: +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
squarez = [value ** 2 for value in range(1, 11)]
print(squarez)

#To use list comprehension syntax, begin with a descriptive name for the list, such as squares. Next, open a set of square brackets and define the expression for the values you want to store in the new list. In this example the expression is value**2, which raises the value to the second power. Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. Note that no colon is used at the end of the for statement.


	# WORKING WITH PART OF A LIST

		# Slicing a List

players = ["Oz", "Maria", "William", "Jeremiah", "Eliz", "Simon", "Jimmy", "Cherry", "Micah", "Israel"]

print(players[1:3])     # print from index 1 to three; remember index 3 is not printed
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")


print(players[:3])      # also prints first three when first index is omitted.
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")


print(players[3:]) # print from fourth index to end when second index is omitted
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")


print(players[-3:]) # print last three elements


print("\n Add steps value to slice: +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
print(players[0:10:3])    # If a third value is included in the brackets indicating a slice, this tells Python how many items to skip between items in the specified range.


print("\n Assign slice to variable +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
sliced_up = [players[0:4]] # assigns slice to variable
print(sliced_up)


    # Looping Through a Slice
    
players = ["Oz", "Maria", "William", "Jeremiah", "Eliz", "Simon", "Jimmy", "Cherry", "Micah", "Israel"]

for player in players[-3:]:
	print(f"{player} plays fine.")
	print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

    # Copying a List
    
my_foodz = ["greens", "garden egg", "egg-plant", "fruits"]

salyz_foodz = my_foodz[:]   # Create a copy by omitting first and second index and assigning slice to new variable

salyz_foodz.append("Chicken")
my_foodz.append("brocoli")

print(salyz_foodz)
print(my_foodz)

# Note that copying is different from setting salyz_foodz equal to my_foodz and will behave differently e.g. when you try to add to the two "separate" lists
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")


    # TUPLES
    
# sometimes you’ll want to create a list of items that cannot change. Tuples allow you to do just that. Python refers to values that cannot change as immutable, and an immutable list is called a tuple. 
# A tuple looks just like a list, except you use parentheses instead of square brackets. Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

# if we have a rectangle that should always be a certain size, we can ensure that its size doesn’t change by putting the dimensions into a tuple:

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

    # Looping through all values in a tuple

for i in dimensions:
	print(i)
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")


# Tuples are technically defined by the presence of a comma; the parentheses make them look neater and more readable. If you want to define a tuple with one element, you need to include a trailing comma: 
# my_t = (3,) 
# It doesn’t often make sense to build a tuple with one element, but this can happen when tuples are generated automatically.


    # Writing over a Tuple

# Although you can’t modify a tuple, you can assign a new value to a variable that represents a tuple.

print("Original dimensions of tuple were: \n")
for i in dimensions:
	print(i)
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

dimensions = 450, 32    # remember tuples are technically defined by a comma
print("Modified dimensions of tuple are \n:")
for i in dimensions:
	print(i)
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")



