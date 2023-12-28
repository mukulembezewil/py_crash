utensils = ["cup", "plate", "spoons", "pans", "forks", "kettle", "flask"]

print(f"Original list ======> \n \n {utensils}")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")


print(f"Temporary sort on display: \n {sorted(utensils)} ")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"Temporary reverse sort on display: \n {sorted(utensils, reverse=True)}")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")


print(f"But note that list is still in original: \n {utensils}")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"Let us alphabetic sort it permanently now: \n")
utensils.sort()
print(utensils)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"And let us alphabetic reverse sort it permanently? : \n")
utensils.sort(reverse=True)
print(utensils)
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"But how many members are in this list? : \n")
print(f"{len(utensils)} members only.")
print("\n+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(utensils)
print("Lastly let us reverse the list as is: \n")
utensils.reverse()
print(utensils)
