# 4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following: 
#• Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list. 
#• Print the message Three items from the middle of the list are:. Then use a slice to print three items from the middle of the list. 
#• Print the message The last three items in the list are:. Then use a slice to print the last three items in the list.

top_tech = ["google", "amazon", "microsoft", "oracle", "adobe", "linux", "facebook", "whatsApp"]

print(f"The first three top_tech players are:\n {top_tech[0:3]}")
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"Three companies from the middle are: \n {top_tech[2:6]}")
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")

print(f"The last three members are: \n {top_tech[-3:]}")
print("\n +-+-+-+-+-+-+-+-+-+-+-+-+-\n")
