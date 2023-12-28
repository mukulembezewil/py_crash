# ORGANIZING A LIST

# sort() method SORTS A LIST PERMANENTLY

cars = ["bmw", "audi", "toyota", "subaru", "mercedes", "mazda"]
cars.sort()
print(cars)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

    # reverse sort a list
cars.sort(reverse=True)
print(cars)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# SORTING THE LIST TEMPORARILY with sorted()

ages = [4, 9, 23, 2, 7, 1]
ages.sort(reverse=True)
print(ages)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

languages= ["python", "javaScript", "ruby", "basic", "C++", "kotlin", "java", "Go"]
print(sorted(languages))
print("\n")
print(sorted(languages, reverse=True))    # reverse simply add second argument reverse=True to sorted() method
# The sorted() function lets you display your list in a particular order, but doesn’t affect the actual order of the list.
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(languages)    # notice list still in original order after sorted() function has been used.
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# TO PRINT LIST IN REVERSE ORDER
beasts = ["lion", "antelope", "tiger", "bear"]
print(beasts)
print("\n")

beasts.reverse()
print(beasts)   
# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list. Note that reverse() changes the order of a list permanently; to reverse it again, reapply method;
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# FINDING THE LENGTH OF A LIST - len(listname)

print("The length of the beasts list is: ")
print(len(beasts))