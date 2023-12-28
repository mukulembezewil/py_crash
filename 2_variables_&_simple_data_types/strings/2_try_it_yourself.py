#Personal Message: Use a variable to represent a person’s name, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

pals_name = "James Bible"
print("Hello " + pals_name + ", would you like to learn some py today?")

#Name Cases: Use a variable to represent a person’s name, and then print that person’s name in lowercase, uppercase, and title case.

lads_name = "TriCia"
print(lads_name.lower())
print(lads_name.upper())
print(lads_name.title())

#Famous Quote: Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”

print('Someone once said, "In times of change the learners will inherit the earth while the learned find themselves beautifully equipped to deal with a world that no longer exists."')

#Famous Quote 2: Repeat Exercise 2-5, but this time, represent the famous person’s name using a variable called famous_person. Then compose your mes- sage and represent it with a new variable called message. Print your message.
famous_person = "Wil"
print(famous_person + ' once said, "Success is the progressive realization of a worthy goal."')

#Stripping Names: Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name_spaces = " Pauline "
print("Auntie" + name_spaces + "is a chiropractor")
print("Auntie" + name_spaces.rstrip() + "is a chiropractor")
print("Auntie" + name_spaces.lstrip() + "is a chiropractor")
print("Auntie" + name_spaces.strip() + "is a chiropractor")

#File Extensions: Python has a removesuffix() method that works exactly like removeprefix(). Assign the value 'python_notes.txt' to a variable called filename. Then use the removesuffix() method to display the filename without the file extension, like some file browsers do.

filename = "python_notes.txt"
print(filename.removesuffix('.txt'))