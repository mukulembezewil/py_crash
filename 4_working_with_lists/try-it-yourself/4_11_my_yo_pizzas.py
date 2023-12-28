# 4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56). 
# Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following: 
# Add a new pizza to the original list. 
# Add a different pizza to the list friend_pizzas. 
# Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.

my_pitsaz = ["nsenene", "vegetable", "mushroom"]

palz_pitsaz = my_pitsaz[:]

my_pitsaz.append("chickeh hawaii")
palz_pitsaz.append("magherita")

print("My favorite pizzas are: \n")
for pizza in my_pitsaz: 
  print(f"⭐ {pizza}")
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
  
  

print("My pal's favorite pizzas are: \n")
for pizza in palz_pitsaz:
  print(f"✡ {pizza}")
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
