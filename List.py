
# ==========================================
# PYTHON LISTS - COMPLETE PRACTICE
# ==========================================

# 1. Creating Lists
fruits = ["apple", "banana", "mango"]
numbers = [10, 20, 30, 40, 50]
mixed = ["Saad", 26, True, 70.5]

print("Fruits:", fruits)
print("Numbers:", numbers)
print("Mixed:", mixed)


# 2. Accessing List Elements (Indexing)
print("\n--- Indexing ---")
print(fruits[0])      # First element
print(fruits[1])      # Second element
print(fruits[-1])     # Last element
print(fruits[-2])     # Second last element


# 3. Slicing Lists
print("\n--- Slicing ---")
print(numbers[0:3])   # Index 0 to 2
print(numbers[:3])    # First 3 elements
print(numbers[2:])    # From index 2 onwards
print(numbers[::-1])  # Reverse list


# 4. Updating Elements
print("\n--- Updating ---")
fruits[0] = "orange"
print(fruits)


# 5. Adding Elements
print("\n--- Adding ---")
fruits.append("grapes")          # Add at end
fruits.insert(1, "pineapple")    # Add at specific index
fruits.extend(["kiwi", "peach"]) # Add multiple elements
print(fruits)


# 6. Removing Elements
print("\n--- Removing ---")
fruits.remove("banana")  # Remove by value
fruits.pop()             # Remove last element
fruits.pop(0)            # Remove by index
print(fruits)

# del numbers[0]  # Delete element by index
# numbers.clear() # Remove all elements


# 7. List Length
print("\n--- Length ---")
print(len(numbers))


# 8. Checking if an Element Exists
print("\n--- Membership ---")
print("mango" in fruits)
print("apple" not in fruits)


# 9. Looping Through a List
print("\n--- For Loop ---")
for fruit in fruits:
    print(fruit)

print("\n--- Enumerate ---")
for index, fruit in enumerate(fruits):
    print(index, fruit)


# 10. Sorting Lists
print("\n--- Sorting ---")
scores = [40, 10, 90, 30, 70]

scores.sort()                 # Ascending
print(scores)

scores.sort(reverse=True)     # Descending
print(scores)

# sorted() returns a new sorted list
new_scores = sorted([40, 10, 90, 30, 70])
print(new_scores)


# 11. Reversing a List
print("\n--- Reverse ---")
scores.reverse()
print(scores)


# 12. Finding Minimum, Maximum and Sum
print("\n--- Calculations ---")
print("Minimum:", min(numbers))
print("Maximum:", max(numbers))
print("Sum:", sum(numbers))


# 13. Counting and Finding Elements
print("\n--- Count and Index ---")
colors = ["red", "blue", "red", "green", "red"]

print(colors.count("red"))  # Count occurrences
print(colors.index("blue")) # Find first index


# 14. Copying Lists
print("\n--- Copy ---")
original = [1, 2, 3]
copied = original.copy()

copied.append(4)

print("Original:", original)
print("Copied:", copied)


# 15. List Concatenation
print("\n--- Concatenation ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

combined = list1 + list2
print(combined)


# 16. List Repetition
print("\n--- Repetition ---")
repeated = [1, 2] * 3
print(repeated)


# 17. List Comprehension
print("\n--- List Comprehension ---")
squares = [x ** 2 for x in range(1, 6)]
print(squares)

# With condition
even_numbers = [x for x in range(1, 11) if x % 2 == 0]
print(even_numbers)


# 18. Nested Lists (2D Lists)
print("\n--- Nested Lists ---")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])       # First row
print(matrix[1][2])    # Second row, third column


# 19. Unpacking Lists
print("\n--- Unpacking ---")
person = ["Saad", 26, "Developer"]

name, age, profession = person

print(name)
print(age)
print(profession)


# 20. Useful Built-in Functions
print("\n--- Built-in Functions ---")
values = [5, 2, 8, 1, 9]

print(len(values))
print(max(values))
print(min(values))
print(sum(values))
print(any(values))
print(all(values))

print("\n--- END OF LISTS PRACTICE ---")
