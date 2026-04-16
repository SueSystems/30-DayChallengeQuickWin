"""Alternative: List Comprehension
If you want to create a new list containing only the names that start with "A" or "a," a list comprehension is the cleanest way:
"""

name = [
    input("Please enter a word: ")
    input("Please enter a word: ")
    input("Please enter a word: ")
    input("Please enter a word: ")
    input("Please enter a word: ")
]
matches = [name for name in names_list if name.lower().startswith('a')]

print(matches)
# Output: ['Akinyi', 'akinyi', 'aoko', 'aora']