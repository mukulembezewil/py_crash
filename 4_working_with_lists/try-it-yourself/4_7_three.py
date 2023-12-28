# 4-7. Threes: Make a list of the multiples of 3, from 3 to 30. Use a for loop to print the numbers in your list.

multiples_of_three = []

for value in range(3, 31):
  multiples_of_three.append(value * 3)
  
print (multiples_of_three)