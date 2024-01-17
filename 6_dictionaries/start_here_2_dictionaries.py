# Python dictionaries are versatile data structures that can store a wide variety of data types. Here are some examples showcasing different types of data that can be stored in dictionaries:

	#	basic dictionary
person = {
	"name": "Jones",
	"age": 18,
	"gender": "male",
	}

	#	nested dictionary

student = {
	"name": "Samalie",
	"age": 26,
	"grades": {
		"maths": 90,
		"science": 95,
		"literature": 99,
		}
	}

	#	list as a value

employee = {
	"name": "Bobs",
	"department": "IT",
	"skills": ['python', 'javascript', 'SQL']
	}

	#	tuple as a key

location = {
	('latitude', 'longitude'): (37.7749, -122.4194),
	'city': 'Kampala',
}

	#	mixed data types

record = {
	"id": 101,
	"name": 'Eva',
	"is_student": True,
	"marks": None,
	"courses": ['Python', 'Java'],
}

	#	dictionary comprehension

numbers = {x:x**2 for x in range(1, 6)}

	#	using different data types as keys

mixed_keys = {
	42: 'Answer',
	(1, 2): 'Tuple key',
	3.14: 'Pi',
	'day': 'Monday',
	}

	#	boolean values

status = {
	'is_online': True,
	'has_permission': False,
	}

	#	function as a value

math_operations = {
	'add': lambda x, y: x + y,
	'subtract': lambda x, y: x - y,
	'multiply': lambda x, y: x * y,
	}

	#	JSON-like structure

person_data = {
	'name': 'Alex',
	'age': 30,
	'address': {
		'street': '123 Main St',
		'city': 'Jinja',
		'zipcode': '256'
		}
	}

# These examples demonstrate the flexibility of Python dictionaries in handling a variety of data types and structures.

# ON DEEP NESTING DICTIONARIES

# While using nested dictionaries in Python is common and often necessary, there are potential downsides and considerations when dealing with deeply nested structures. 

# To mitigate these issues, consider using alternative data structures, such as classes or named tuples, to represent structured data in a more organized and readable way. Additionally, breaking down complex nested dictionaries into smaller, more manageable pieces or using helper functions to access nested values can improve code readability and maintainability. Always aim for a balance between the depth of nesting and the readability of your code.

	#	EXAMPLES OF HOW TO MANIPULATE DATA IN EACH OF THE DICTIONARIES ABOVE

# Example Dictionary - BASIC DICTIONARY
person = {'name': 'John Doe', 'age': 25, 'gender': 'Male'}

# Accessing values
print(person['name'])  # Output: John Doe

# Modifying values
person['age'] = 26

# Adding a new key-value pair
person['city'] = 'New York'

# Removing a key-value pair
del person['gender']

print(person)
# Output: {'name': 'John Doe', 'age': 26, 'city': 'New York'}

###############################################################

# Example Dictionary - NESTED DICTIONARY
student = {'name': 'Alice', 'age': 20, 'grades': {'math': 90, 'english': 85, 'science': 92}}

# Accessing nested values
print(student['grades']['math'])  # Output: 90

# Modifying nested values
student['grades']['math'] = 95

# Adding a new subject
student['grades']['history'] = 88

print(student)
# Output: {'name': 'Alice', 'age': 20, 'grades': {'math': 95, 'english': 85, 'science': 92, 'history': 88}}

################################################################

# Example Dictionary - LIST AS A VALUE
employee = {'name': 'Bob', 'department': 'IT', 'skills': ['Python', 'JavaScript', 'SQL']}

# Accessing list elements
print(employee['skills'][0])  # Output: Python

# Modifying list elements
employee['skills'].append('Java')

# Removing a skill
employee['skills'].remove('JavaScript')

print(employee)
# Output: {'name': 'Bob', 'department': 'IT', 'skills': ['Python', 'SQL', 'Java']}

###############################################################

# Example Dictionary - TUPLE AS A KEY
location = {('latitude', 'longitude'): (37.7749, -122.4194), 'city': 'San Francisco'}

# Accessing values with a tuple key
print(location[('latitude', 'longitude')])  # Output: (37.7749, -122.4194)

# Modifying values
location[('latitude', 'longitude')] = (37.75, -122.45)

print(location)
# Output: {('latitude', 'longitude'): (37.75, -122.45), 'city': 'San Francisco'}

###############################################################

# Example Dictionary - MIXED DATA TYPES
record = {'id': 101, 'name': 'Eva', 'is_student': True, 'marks': None, 'courses': ['Python', 'Java']}

# Checking if a key exists
if 'marks' in record:
    # Modifying value
    record['marks'] = 85
else:
    # Adding a new key-value pair
    record['marks'] = 85

print(record)
# Output: {'id': 101, 'name': 'Eva', 'is_student': True, 'marks': 85, 'courses': ['Python', 'Java']}

###############################################################

# Example Dictionary - DICTIONARY COMPREHENSION
numbers = {x: x**2 for x in range(1, 6)}

# Accessing values
print(numbers[3])  # Output: 9

# Modifying values
numbers[4] = 16

# Removing a key-value pair
del numbers[2]

print(numbers)
# Output: {1: 1, 3: 9, 4: 16, 5: 25}

###############################################################

