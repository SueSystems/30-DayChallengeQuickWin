"""
How are elements of a string accessed example Akinyi, akinyi, pauline, aoko, aora to check if they start with "a " or "A"
first need to turn that single string into a list of individual names. Once they are separated, you can access each one and check the first letter.
Here is the most efficient way to do it:

1. Separate the String
First, use .split(", ") to turn your string into a list so you can look at each name individually.

2. Check the Condition
You can check the first character using indexing (e.g., name[0]) or the built-in .startswith() method.

names_string = "Akinyi, akinyi, pauline, aoko, aora"

# Step 1: Convert to a list
names_list = names_string.split(", ")

# Step 2: Access and check each element
for name in names_list:
    # .lower() makes the check case-insensitive (catches both 'A' and 'a')
    if name.lower().startswith('a'):
        print(f"Match found: {name}")

Alternative: List Comprehension
If you want to create a new list containing only the names that start with "A" or "a," a list comprehension is the cleanest way:
matches = [name for name in names_list if name.lower().startswith('a')]

print(matches)
# Output: ['Akinyi', 'akinyi', 'aoko', 'aora']

Why this works:
.split(", "): This removes the commas and spaces, leaving you with just the names.

Indexing [0] vs .startswith(): While name[0].lower() == 'a' works, .startswith() is generally safer because it won't crash if it encounters an empty string.

.lower(): This is a great "normalization" trick. Instead of checking if name.startswith('a') or name.startswith('A'), converting the name to lowercase once allows you to handle both cases in one go.
"""