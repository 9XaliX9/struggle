# Hash Table:

# A hash table is a data structure that implements an associative array abstract data type.
# It uses a hash function to compute an index into an array of buckets or slots, from which
# the desired value can be found.

# Basic operations on a hash table:
# - Insert: Adds a key-value pair to the hash table.
# - Search: Finds the value associated with a given key.
# - Delete: Removes a key-value pair from the hash table.

# ----------------------------------------------------------
# Hashing:

# Hashing is a process used to map data of arbitrary size to fixed-size values.
# A hash function is used to generate the hash code, which is then used as an index in a data structure (usually an array).

# Building A Hash Table from Scratch

# We will build the Hash Set in 5 steps:

# Starting with an array.
# Storing names using a hash function.
# Looking up an element using a hash function.
# Handling collisions.
# The basic Hash Set code example and simulation.

# print("\033[95m\n{------------------------------")


# """ Step1 : Starting with an array"""

# my_array = ["Pete", "Jones", "Lisa", "Bob", "ali"]

# my_hash_set = [None, None, None, None, None, None, None, None, None, None]


# """Step 2 : Storing names using a hash function."""

# def hash_function(value):
#     sum_of_chars = 0
#     for char in value:
#         sum_of_chars += ord(char)

#     return sum_of_chars % 10

# print("'Bob' has hash code:", hash_function("Bob"))


# """ Step 3: Looking up a name using a hash function"""

# my_hash_set = [None, "Jones", None, "Lisa", None, "Bob", None, "ali", "Pete", None]

# def hash_function(value):
#     sum_of_chars = 0
#     for char in value:
#         sum_of_chars += ord(char)

#     return sum_of_chars % 10

# def contains(name):
#     index = hash_function(name)
#     return my_hash_set[index] == name

# print("'Pete' is in the Hash Set:", contains("Pete"))
# print("'Pete' is in the Hash Set:", hash_function("Pete"))

# """ Step 4: Handling collisions"""

# my_hash_set = [
#     [None],
#     ["Jones"],
#     [None],
#     ["Lisa", "Stuart"],
#     [None],
#     ["Bob"],
#     [None],
#     ["ali"],
#     ["Pete"],
#     [None],
# ]

# """ Step 5 : Hash Set code example and simulation"""
# my_hash_set = [
#     [None],
#     ["Jones"],
#     [None],
#     ["Lisa"],
#     [None],
#     ["Bob"],
#     [None],
#     ["ali"],
#     ["Pete"],
#     [None],
# ]

# def hash_function(value):
#     return sum(ord(char) for char in value) % 10

# def add(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     if value not in bucket:
#         bucket.append(value)

# def contains(value):
#     index = hash_function(value)
#     bucket = my_hash_set[index]
#     return value in bucket

# add("Stuarft")

# print(my_hash_set)
# print("Contains Stuart:", contains("Stuarft"))
# print("'Stuart' is in the Hash Set:", hash_function("Stuarft"))
# print("'lisa' is in the Hash Set:", hash_function("lisa"))


# print("\n------------------------------}\n\033[0m")


# Uses of Hash Tables
# Hash Tables are great for:

# 1) Checking if something is in a collection (like finding a book in a library).
# 2) Storing unique items and quickly finding them (like storing phone numbers).
# 3)Connecting values to keys (like linking names to phone numbers).

# Most important reason why Hash Tables are great is that H.T are very fast compared Arrays and Linked Lists, especially for large sets.
# Arrays and Linked Lists have time complexity O(n)
# for search and delete, while Hash Tables have just O(1)
#  on average! Read more about time complexity here.

# -----------------------------------------------------------------------------------------------------------------
# Hash Tables Summarized

# Hash Table elements are stored in storage containers called buckets.

# Every Hash Table element has part that is unique that is called the key.

# A hash function takes the key of an element to generate a hash code.

# The hash code says what bucket element belongs to, so we can go directly to that Hash Table element:
#     to modify it, or to delete it, or just to check if it exists.
#     Specific hash functions are explained in detail on the next two pages.

# A collision happens when two Hash Table elements have the same hash code,
# because that means they belong to the same bucket. A collision can be solved in two ways.

# Chaining is the way collisions are solved, by using arrays or linked lists to allow more than one element in same bucket.

# Open Addressing is another way to solve collisions. With open addressing,
# if we want to store an element but there is already an element in that bucket,
#  the element is stored in the next available bucket.
#  This can be done in many different ways,but we will not explain open addressing any further here.

# Conclusion
# Hash Tables are powerful tools in programming, helping you to manage and access data efficiently.

# Whether you use a Hash Set or a Hash Map depends on what you need:
#  just to know if something is there, or to find detailed information about it.


print("\033[95m\n{------------------------------")

hash_set = [None] * 10


# def hash_function(value):
#     sum_c = 0
#     for char in value:
#         sum_c += ord(char)
#     return sum_c % 10
# smart way down

def hash_function(value):
    return sum(ord(char) for char in value) % 10

def add(value):
    index = hash_function(value)
    if hash_set[index] is None:
        hash_set[index] = [value]
    else:
        hash_set[index].append(value)
    print(f"{value.title():<7}: {index}")  # this always gets printed

def contains(value):
    index = hash_function(value)
    if hash_set[index] in hash_set:
        print(f"Yes! value '{value} is at index '{index}' ")

add("ali")
add("hashim")
add("aliza")
add("alex")
add("hasan")
add("mina")
print("\n")

contains("alex")

# for i in hash_set:

#     if i == None:
#         index = hash_set.index(i)
#         print("index are empty:",index) #do not use this.  it will give you the last element's index, which is wrong.

for index, value in enumerate(hash_set):
    if value is None: # where ever value is none its gonna print index +1 like a counter
        print(f"empty slot at index: {index}")

print(hash_set)

print("\n------------------------------}\n\033[0m")
