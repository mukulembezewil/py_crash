# 5-1. Conditional Tests: Write a series of conditional tests. Print a statement describing each test and your prediction for the results of each test.

breakfast = "salami"
print("Is breakfast today Salami? I predict True.")
print('\n--------------------------------\n')
print(breakfast == "salami")
print('\n--------------------------------\n')

pay_method = "card"
print("Is client paying with cash? False!")
print('\n--------------------------------\n')
print(pay_method == "cash")
print('\n--------------------------------\n')

user_name = "Trudie"
print("User name already exists. I say True.")
print('\n--------------------------------\n')
print(user_name == "Trudie")
print('\n--------------------------------\n')

# Look closely at your results, and make sure you understand why each line evaluates to True or False. 

# Create at least 10 tests. Have at least 5 tests evaluate to True and another 5 tests evaluate to False.

meet_time = "evening"
print("What time is the session? I say morning.")
print('\n--------------------------------\n')
print(f"{meet_time == 'morning'}! Meet is in the evening")
print('\n--------------------------------\n')

paid = "yes"
print("Client has already paid. I predict no.")
print('\n--------------------------------\n')
print(paid == "no")