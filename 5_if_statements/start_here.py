# IF STATEMENTS

# Python’s if statement allows you to examine the current STATE of a program and respond apprOpriately to that STATE.

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

	# CONDITIONAL TESTS

# At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.

	# Checking for Equality ==

		#The simplest conditional test checks whether the value of a variable is equal to the value of interest:

car = "bmw"
print(car == "bmw")	# True

	# Case Sensitive

# Testing for equality is case sensitive in Python.

car = "Audi"
print(car == "audi")	# False

# if case doesn’t matter and instead you just want to test the value of a variable, you can convert the variable’s value to lowercase before doing the comparison:

car = "toyota"
print(car.lower() == "toyota")	# True
# Returns True because the test is now case insensitive
print(car)
# Note that the value stored in car has not been affected by the lower() method.

	# Checking for InEquality !=

requested_topping = "mushrooms"

if requested_topping != "anchovies":
    print("Please take back your anchovies!")

# Numerical Comparisons

age = 18
print(age == 18)	# True

answer = 17
if answer != 42:
    print("Pal, that is not the correct answer.")

# Other mathematical Comparisons (<, <=, >, <=, etc)

	# CHECKING MULTIPLE CONDITIONS USING and/or

age_1 = 22
age_2 = 18

print(age_1 >=21 and age_2 >=21)	# False
print(age_1 >= 18 and age_2 >= 18)	# True

print(age_1 > 18 or age_2 == 16)	# True
print(age_1 < 20 or age_2 > 60)	# False 
# An or expression fails only when both individual tests fail.

# To improve readability, you can use parentheses around the individual tests, but they are not required: 
age_2 = 24

if (age_1 >= 21) and (age_2 >= 21):
    print("Yep, this' true.")


	# Checking Whether a Value Is/not in a List Using in /not it

pizzas = ['mozzareli', 'hindu', 'krishna', 'vegan']

print("hindu" in pizzas)
print("pepperoni" not in pizzas)
print("\n+++++++++++++++++++\n")


banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f'{user.title()}, you are welcome to post a comment.')

print("\n+++++++++++++++++++\n")

	# BOOLEAN EXPRESSIONS

# Boolean expression is just another name for a conditional test. 
# A Boolean value is either True or False. Boolean values are often used to keep track of certain conditions e.g.
game_active = True
can_edit = False

	# if STATEMENTS

		# SImple if Statements

print('\n-----Of Voting Age?-----\n')

age = 19
if age >= 18:		# Note you could put the boolean expression in ()
    print("You are grown enough to vote.")
    print("Have you registered to vote yet?")

		# if-else statement

print('\n-----Of Voting Age Yet?-----\n')
age = 16

if age >= 18:	# Note you could put the boolean expression in ()
    print("You are grown enough to vote")
    print("Have you registered to vote yet?")
else:
    print("Ya a lil too young to vote.")
    print("Pliz register to vote soon as you clock 18😉.")

		# The if-elif-else Chain

print('\n-----Zoo Entrance fee-----\n')
age = 34

if age < 4:
    print("Free admissi😜n")
elif age >= 4 and age < 18:		# Note you could have simply <18
    print("Children to Teen entrance: $25")
else:
    print("Adult entrance: $40 only.")

# it would be more concise to set just the price inside the if-elif-else chain and then have a single print() call that runs after the chain has been evaluated:

print('\n-----Cinema Entrance fee-----\n')
age = 16

if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission fee is: ${price} only")

		# Using Multiple elif Blocks

print('\n-----Elderly Cinema Entrance fee-----\n')
age = 45

if age < 4:
    price = 0
    design = "a baby"
elif age < 18:
    price = 25
    design = "an infant or teen"
elif age < 65:
    price = 40
    design = "an adult"
elif age >= 65:
    price = 20
    design = "a Senior citizen"
print(f"As {design}, your admission fee is: ${price} only")

# In the above you could use the else block in place of the last elif block.
	# else:
		# price = 20
		# design = "a Senior citizen"
# Python does not require an else block at the end of an if-elif chain. Sometimes, an else block is useful. Other times, it’s clearer to use an additional elif statement that catches the specific condition of interest.
# The final elif block assigns a price of $20 when the person is 65 or older, which is a little clearer than the general else block. With this, every block of code must pass a specific test in order to be executed. 
# The else block is a catchall statement. It matches any condition that wasn’t matched by a specific if or elif test, and that can sometimes include invalid or even malicious data. 
# If you have a specific final condition you’re testing for, consider using a final elif block and omit the else block. As a result, you’ll be more confident that your code will run only under the correct conditions.


		# Testing Multiple Conditions

# If you want only one block of code to run, use an if-elif-else chain. If more than one block of code needs to run, use a series of indepen- dent if statements.

requested_spread = ["butter", "mamalade"]
print('\n-----Preparing bread toast-----\n')

if "butter" in requested_spread:
    print("Adding butter")

if "jam" in requested_spread:
    print("Adding red jam")

if "mamalade" in requested_spread:
    print("Adding golden mamalade")

print("\n🤤Your toast is ready to chew")

# This code would not work properly if we used an if-elif-else block, because the code would stop running after only one test passes.


		# USING if STATEMENTS WITH LISTS

	# Checking for Special Items

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
	if requested_topping == "green peppers":
		print("Apologies. We're fresh out of peppers.🤗")
	else:
		print(f"Adding {requested_topping}")
print('\nYour pizza is ready to deliver.')
print('\n_____________________________________\n')

		# Checking that a list is not empty
requested_topups = []

if requested_topups:
	for topup in requested_topups:
		print(f'Adding {topup}')
	print(f'Finished baking your pizza.')
else:
	print("Are you sure you want a plain pizza?")

# When the name of a list is used in an if statement, Python returns True if the list contains at least one item; an empty list evaluates to False

	# Using Multiple Lists

available_condiments = ('mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheeses')

requested_condiments = ['mushrooms', 'french fries', 'extra cheeses']

for condiment in requested_condiments:
	if condiment in available_condiments:
		print(f'Adding {condiment}')
	else:
		print(f"Cheiii sorry. We do not have {condiment} at the moment.")
print('\n_____________________________________\n')
print("Your large-size pizza is ready to pick.")