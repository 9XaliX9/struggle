# Hash Sets
# A Hash Set is form of Hash Table data structure that usually
# holds a large number of elements.

# Using a Hash Set we can search, add, and
#  remove elements really fast.

# A Hash Set stores unique elements in buckets according
# to the element's hash code.

# Hash code: A number generated from an element's unique value (key)
# , to determine what bucket that Hash Set element belongs to.

# Unique elements: A H.S cannot have more than one element with same value.

# Bucket: A H.S consists of many such buckets, or containers, to store elements.
# If two elements have same hash code, they belong to same bucket.
# The buckets are therefore often implemented as arrays or linked lists,
# because a bucket needs to be able to hold more than one element.

"""Hash Sets in Python are typically done by using Python's own 
set data type, but to get better understanding of how Hash 
Sets work we will not use that here."""


print("\033[95m\n{------------------------------")


# class SimpleHashSet:
#     def __init__(self, size=100):
#         self.size = size
#         self.bucket = [[] for i in range(size)]

#     def hash_function(self, value):
#         return sum(ord(char) for char in value)% self.size

#     def add(self,value):
#         index  = self.hash_function(value)
#         bucket =  self.bucket[index]
#         if value not in bucket:
#             bucket.append(value)

#     def contains(self, value):
#         index = self.hash_function(value)
#         bucket = self.bucket[index]
#         return value in bucket

#     def remove(self, value):
#         index = self.hash_function(value)
#         bucket = self.bucket[index]
#         if value in bucket:
#             bucket.remove(value)

#     def print_set(self):
#         print("hash set contents:" )
#         for index, bucket in enumerate(self.bucket):
#             print(f"{index} : {bucket}")

# # Initialize an empty hash set
# hash_set = SimpleHashSet(size=10)

# hash_set.add("Charlotte")
# hash_set.add("Thomas")
# hash_set.add("Jens")
# hash_set.add("Peter")
# hash_set.add("Lisa")
# hash_set.add("Adele")
# hash_set.add("Michaela")
# hash_set.add("Bob")

# hash_set.print_set()

# print("\n'Peter' is in the set:",hash_set.contains('Peter'))
# print("Removing 'Peter'")
# hash_set.remove('Peter')
# print("'Peter' is in the set:",hash_set.contains('Peter'))
# print("'Adele' has hash code:",hash_set.hash_function('Adele'))
# =============================================================================================
# practices


# class SimpleHashSet:
#     def __init__(self, size=100):
#         self.size = size
#         self.bucket = [[] for i in range(size)]  # a list

#     def hash_function(self, value):
#         return sum(ord(char) for char in value) % 10

#     def add(self, value):
#         index = self.hash_function(value)
#         bucket = self.bucket[index]
#         if value not in bucket:
#             bucket.append(value)
#         else:
#             print(f"'{value:<3}' already exists.")

#     def contains(self, value):
#         index = self.hash_function(value)
#         bucket =self.bucket[index]

#         print(f"'{value:<3}' is in the hash set.")
#         return value in bucket

#     def remove(self, value):
#         index = self.hash_function(value)
#         bucket = self.bucket[index]
#         if value in bucket:
#             bucket.remove(value)
#             print(f"\n'{value:<3}' Removed successfully!")
#         else:
#             print(f"'{value:<3}' not in hash set.")

#     def print_set(self):
#         print("\ncontent of hash set: ")
#         for counter, value in enumerate(self.bucket):
#             print(f"Index {counter}: {value}")

#     def empty_indexes(self):
#             empty_indexes=[]
#             for counter, bucket in enumerate(self.bucket):
#                 if not bucket:
#                     empty_indexes.append(counter)
#                     print(f"Index {counter}: are empty.")
#             return empty_indexes

# hash_set = SimpleHashSet(10)

# hash_set.add("a")
# hash_set.add("a")
# hash_set.add("b")
# hash_set.add("c")
# hash_set.add("d")
# hash_set.add("e")
# hash_set.add("f")
# hash_set.add("g")
# hash_set.add("h")
# hash_set.add("i")
# hash_set.add("j")
# hash_set.add("k")

# hash_set.remove("k")
# hash_set.remove("a")
# hash_set.remove("b")
# hash_set.remove("ke")
# hash_set.remove("g")
# hash_set.remove("q")

# hash_set.contains('a')
# hash_set.empty_indexes()

# hash_set.print_set()
# ==============================================================================================================
# practices2:


class SimpleHashSet:
    def __init__(self, size=100):
        self.size = size
        self.bucket = [[] for i in range(size)]

    def hash_function(self, value):
        return sum(ord(char) for char in value) % 10  # give index

    def add(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]
        if value not in bucket:
            bucket.append(value)
        else:
            print("\033[91m{")
            print(f" '{value}' already exists!")
            print("}\033[0m")

    def remove(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]

        if value in bucket:
            bucket.remove(value)
            print(f" '{value:<5}' removed successfully! from index: '{index}'")

    def contains(self, value):
        index = self.hash_function(value)
        bucket = self.bucket[index]
        print(f"'{value}' is in the hash set!? ")
        return value in bucket

    def empty_indexes(self):
        empty_indexes = []
        print("\033[95mEmpty indexes:\n")
        for counter, bucket in enumerate(self.bucket):
            if not bucket:
                empty_indexes.append(counter)

                print(f"Index '{counter}' is empty.")
        print("\033[0m")
        return empty_indexes

    def print_set(self):
        print("\n\033[96m{\n Set Content:\033[96m \n")

        for counter, value in enumerate(self.bucket):
            print(f" {counter} : {value}")
        print("}\033[95m")


hash_set = SimpleHashSet(10)


hash_set.add("ali")
hash_set.add("ali")
hash_set.add("bgr")
hash_set.add("alir")
hash_set.add("alie")
hash_set.add("alti")
hash_set.add("aldgi")
hash_set.add("qwt")
hash_set.add("alp")
hash_set.add("c")
hash_set.add("f")
hash_set.add("fg")


print("\033[92m\n{")
hash_set.remove("fg")
hash_set.remove("alp")
hash_set.remove("ali")
hash_set.remove("alti")
hash_set.remove("qwt")
print("}\033[0m\n")

print(hash_set.contains("bgr"))  # True after removing
print(hash_set.contains("ali"))  # False after removing
print("\n")


hash_set.empty_indexes()

hash_set.print_set()

print("\n------------------------------}\n\033[0m")
