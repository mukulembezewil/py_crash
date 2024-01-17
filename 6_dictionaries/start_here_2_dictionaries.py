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