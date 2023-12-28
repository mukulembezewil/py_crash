# TO CREATE A LIST
# TO ACCESS ELEMENTS IN A LIST -> listname[index]
# USE STRING METHODS ON ANY ELEMENT IN A LIST
# SPECIAL SYNTAX FOR ACCESSING LAST ELEMENT IN A LIST
# USE INDIVIDUAL VALUES FROM A LIST
	# Pull the first bicycle from list and compose a message using the value.
## MODIFYING, ADDING, AND REMOVING ELEMENTS ##
# Modifying Elements in a list
# Adding Elements to a list -> append(), insert()
# REMOVING ELEMENTS FROM A LIST -> del, pop(), remove()
    # using the del statement - if you know the position of the item you want to remove
    # using the pop() method
    # pop() items from any position -> include index of item in pop() parenthesis
# REMOVING AN ITEM BY VALUE - remove()
# ORGANIZING A LIST



# A List is collection of items in a particular order. Because a list always contains more than one element, it is a good idea to make the name of a list plural.

# TO CREATE A LIST

bicycles = ["trek", "redline", "cannondale", "specialized"]
print(bicycles)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

grade2marks = [70, 85]
print(grade2marks)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


# TO ACCESS ELEMENTS IN A LIST -> listname[index]

print(bicycles[0])
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# USE STRING METHODS ON ANY ELEMENT IN A LIST

print(bicycles[1].title())
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# SPECIAL SYNTAX FOR ACCESSING LAST ELEMENT IN A LIST

print(bicycles[-1]) # this prints last element
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print(bicycles[-3]) # this prints third last element
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# USE INDIVIDUAL VALUES FROM A LIST
  # Pull the first bicycle from list and compose a message using the value.
  
message = (f"My first bicycle was of a {bicycles[3].title()} brand.")
print(message)
gratitude = bicycles[1]
print(f"{gratitude.title()} is a bicycle Mosaic highly recommends.")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")



## MODIFYING, ADDING, AND REMOVING ELEMENTS ##

# Modifying Elements in a list

bicycles[2] = "phoenix"
print(bicycles)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


# Adding Elements to a list -> append(), insert()

bicycles.append("dirtbike-pro")   # appends element to end of list
print(bicycles)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

newbikes = []       # you can start with an empty list and populate it.
newbikes.append("roadmaster")
newbikes.append("ice-mount")
newbikes.append("racer")

print(newbikes)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

newbikes.insert(0, "whoosh") # insert new element at specified position
print(newbikes)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
newbikes.insert(2, "mwasadyuty") # insert new element at specified position
print(newbikes)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# REMOVING ELEMENTS FROM A LIST -> del, pop(), remove()

    # using the del statement - if you know the position of the item you want to remove
    
del newbikes[1]
print(newbikes)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
    
    # using the pop() method
popped_newbike = newbikes.pop()     # pop() method lets you work with item after removing it, by enabling you assign it to a variable.
print(newbikes)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")
print(f"The last new bike I owned was a {popped_newbike.title()}.")

    # pop() items from any position -> include index of item in pop() parenthesis

newbikes.pop(1)
print(newbikes)
# If you’re unsure whether to use the del statement or the pop() method, here’s a simple way to decide: when you want to delete an item from a list and not use that item in any way, use the del statement; if you want to use an item as you remove it, use the pop() method.
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

# REMOVING AN ITEM BY VALUE - remove()

print(bicycles)
bicycles.remove("specialized")
print(bicycles)
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")

removed_item = "phoenix"
bicycles.remove(removed_item)
print(f"\n {removed_item.title()} is a masculine machine.")
print("+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-")


# ORGANIZING A LIST
