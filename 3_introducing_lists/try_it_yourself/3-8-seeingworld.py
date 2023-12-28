# 3-8. SEEING THE WORLD: Think of at least five places in the world you’d like to visit. 


# 1. Store the locations in a list. Make sure the list is not in alphabetical order. 

to_visit = ["tokyo", "sydney", "london", "ny", "toronto", "berlin"]

# 2. Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list.
 
print(f"2. Below is the original list: \n \n{to_visit}")
print("\n 3. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# 3. Use sorted() to print your list in alphabetical order without modifying the actual list. 
print("See temporarily sorted list below: \n")
print(sorted(to_visit))
print("\n 4. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# 4. Show that your list is still in its original order by printing it. 
print((f"But note that the list is still in original order even after using sorted() method: \n"))
print(to_visit)
print("\n 5. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# 5. Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list. 

print(f"Now here's the original list in reverse ALPHABETIC order: ")
print(sorted(to_visit, reverse=True))

# 6. Show that your list is still in its original order by printing it again.
print(to_visit)
print("\n 7.+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")


# 7. Use reverse() to change the order of your list again. Print the list to show it’s back to its original order. 

to_visit.reverse()
print(to_visit)
print("\n 8. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# 8. Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed. 

to_visit.sort()
print(to_visit)
print("\n 9. +-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

# 9. Use sort() to change your list so it’s stored in reverse-alphabetical order. Print the list to show that its order has changed.
to_visit.sort(reverse=True)
print(to_visit)