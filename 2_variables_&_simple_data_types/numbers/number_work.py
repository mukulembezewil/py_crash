#INTEGERS

print(2 + 3)
print(4 * 8)
print (13/2)
print (10/2) #When you divide any two numbers, even if they are integers that result in a whole number, you’ll always get a float
print (87 - 7)
print ( 6 ** 6)   #exponentiation
print( 9 - 3.8)   #If you mix an integer and a float in any other operation, you’ll get a float as well:
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


#FLOATS - any no. with a decimal point
print(3 * 0.1)
print(0.2+0.1)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


#UNDERSCORES IN NUMBERS - you can group digits using underscores to make large numbers more readable:

universe_age = 14_000_000_000_450
print(universe_age)   
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


#Python prints only the digits
#underscore is ignored when storing these kinds of values
#works for both integers and floats

#MULTIPLE ASSIGNMENTS - assign values to more than one variable using just a single line of code
    #separate the variable names with commas
    #do the same with the values
    #number of values must match no. of variables
age, name, height = 2, "Peter", 7
print(height)
print(name)
print(age)
print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _\n")


#CONSTANTS - a constant is a variable whose value changeth not throughout the life of the program.
    #write the variable name in ALL_CAPITAL letters if you want to treat it as constant
    #Python has no built in constant types
    #Python programmers use all-CAPS to indicate constant variable
    
MAX_CONTACTS = 100

