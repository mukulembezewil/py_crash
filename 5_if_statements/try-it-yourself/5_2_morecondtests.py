# 5-2. More Conditional Tests: 
# You don’t have to limit the number of tests you create to 10. If you want to try more comparisons, write more tests. Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings
first_name = "benson"
print('\n-----first_name == Benson?-----\n')
print(first_name == "Benson")
print('\n-----first_name == benson?-----\n')
print(first_name == "benson")

# Tests using the lower() method
last_name = "Mukulembeze"
print('\n------last_name == mukulembeze-----\n')
print(last_name.lower() == "mukulembeze")

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to 
size_10_qty = 200
size_11_qty = 134
size_12_qty = 72
restock_level = 45

print('\n-----size_10_qty >= restock_level-----\n')
print(size_10_qty >= restock_level)

print('\n-----size_11_qty > size_10_qty-----\n')
print(size_11_qty > size_10_qty)

print('\n-----size_12_qty < restock_level-----\n')
print(size_12_qty < restock_level)

print('\n-----restock_level <= size_10_qty-----\n')
print(restock_level <= size_10_qty)

# Tests using the and keyword and the or keyword 
print('\n-----size_11_qty > restock_level and > 120-----\n')
print(size_11_qty > restock_level and size_11_qty > 120)

print('\n-----size_10_qty == 500 or > size_11_qty-----\n')
print(size_10_qty == 500 or size_10_qty > size_11_qty)


# Test whether an item is in a list 
print('\n-----beans among the sauces?-----\n')
sauces = ['peas', 'eshabwe', 'beans', 'gnut paste', 'beef stew', 'chicken gravy']
print("gnut paste" in sauces)

# Test whether an item is not in a list
print('\n-----peas not among the sauces?-----\n')
print("peas" not in sauces)
