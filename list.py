# Creating a sample list
numbers = [3, 1, 4, 1, 5, 9]

# List Methods
numbers.append(2)  # Adds 2 to the end
print("append:", numbers)

numbers.extend([6, 7])  # Extends list with another list
print("extend:", numbers)

numbers.insert(2, 10)  # Inserts 10 at index 2
print("insert:", numbers)

numbers.remove(1)  # Removes the first occurrence of 1
print("remove:", numbers)

popped = numbers.pop()  # Removes and returns the last element
print("pop:", numbers, "| Popped:", popped)

numbers.sort()  # Sorts the list in ascending order
print("sort:", numbers)

numbers.reverse()  # Reverses the list
print("reverse:", numbers)

copy_list = numbers.copy()  # Copies the list
print("copy:", copy_list)

numbers.clear()  # Clears the list
print("clear:", numbers)

# Reset numbers for function examples
numbers = [3, 1, 4, 1, 5, 9]

# List Functions
print("len:", len(numbers))  # Returns length of list
print("max:", max(numbers))  # Returns maximum value
print("min:", min(numbers))  # Returns minimum value
print("sum:", sum(numbers))  # Returns sum of elements

sorted_list = sorted(numbers)  # Returns sorted list
print("sorted:", sorted_list)

any_result = any(numbers)  # True if at least one element is non-zero
print("any:", any_result)

all_result = all(numbers)  # True if all elements are non-zero
print("all:", all_result)

indexed = list(enumerate(numbers))  # Returns index-value pairs
print("enumerate:", indexed)

# Using map to square each element
squared = list(map(lambda x: x**2, numbers))
print("map (square):", squared)

# Using filter to get only even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print("filter (evens):", evens)

# Using zip to pair elements with their index
zipped = list(zip(numbers, squared))
print("zip:", zipped)
