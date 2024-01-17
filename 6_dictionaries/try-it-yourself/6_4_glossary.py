# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output

glossary = {
    "Dictionary": "A key-value pair data structure",
    "Tuple": "An immutable list",
    "Internet": "A network of networks around the globe",
    "Set": "Collection of unique and unordered elements enclosed in curly braces {}",
    "List": "A built-in data type that is used to store a collection of ordered elements",
    }

for word, definition in glossary.items():
    print(f"{word.upper()}: \n{definition}\n")
