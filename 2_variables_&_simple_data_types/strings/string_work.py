#CHANGING STRING TO UPPERCASE

my_first_string = "My God is God"
print(my_first_string.upper())

#CHANGING STRING TO lowercase

my_second_string = "IN THE BEGINNING IS THE WORD."
print(my_second_string.lower())

#CHANGING STRING TO Title Case
my_third_string = "bUILDers of the adYTUM"
print(my_third_string.title())

#USING VARIABLES IN STRINGS - place the letter f immediately before the opening quotation mark 1. Put braces around the name or names of any variable you want to use inside the string. These strings are called f-strings. The f is for format, because Python formats the string by replacing the name of any variable in braces with its value.
acronym_letter_1 = "the"
acronym_letter_2 = "international"
acronym_letter_3 = "developers"
acronym_letter_4 = "association of"

full_acronym = f"We are {acronym_letter_1.title()} {acronym_letter_2.title()} {acronym_letter_4.title()} {acronym_letter_3.title()}"

print(full_acronym)

#ADDING WHITESPACE TO STRINGS WITH TABS OR NEWLINES

  #use \t to add a tab

no_tab = "Python"  
print(no_tab)

yes_tab = "\tPython"
print(yes_tab)

  #use \n to add a new line
print("Languages: \nC \nC# \nC++ \nJava \nJavaScript")

  #combine tabs and new lines: note that new line must come first or the tab won't work.
print("Languages: \n\tC \n\tC# \n\tC++ \n\tJava \n\tJavaScript")

#STRIPPING WHITESPACE- use rstrip() or lstrip() strip() on string to strip off right and left whitespace
  #favorite_language = "English "
  #string above has right whitespace - To remove the whitespace from the string permanently, you have to associate the stripped value with the variable name as below;
  #favorite_language = favorite_language.rstrip()


#REMOVING PREFIXES - use removeprefix()
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

  #Note: Like the methods for removing whitespace, removeprefix() leaves the original string unchanged. If you want to keep the new value with the pre- fix removed, either reassign it to the original variable or assign it to a new variable:
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)