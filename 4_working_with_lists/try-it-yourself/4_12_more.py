# 4-12. More Loops: All versions of foods.py in this section have avoided using for loops when printing, to save space. Choose a version of foods.py, and write two for loops to print each list of foods.

my_foodz = ["greens", "garden egg", "egg-plant", "fruits"]

salyz_foodz = my_foodz[:]   # Create a copy by omitting first and second index and assigning slice to new variable

salyz_foodz.append("Chicken")
my_foodz.append("brocoli")

for food in my_foodz:
  print(food)
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

for item in salyz_foodz:
  print(item)