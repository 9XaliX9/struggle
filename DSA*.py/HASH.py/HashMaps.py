# Hash Maps:

# A Hash Map is a form of Hash Table Data.S that usually holds large number of entries.

# Using Hash Map we can search, add, modify, and remove entries really fast.

# Hash Maps are used to find detailed information about something.

# In simulation below, people are stored in a Hash Map. A person can be looked up
# using a person's unique social security number (the Hash Map key),
# and then we can see that person's name (the Hash Map value).


# It is easier to understand how Hash Maps work if you know about Hash Tables and Hash Sets.

# It is also important to understand the meaning of the words below.

# Entry     : Consists of a key and a value, forming a key-value pair.

# Key       : Unique for each entry in the Hash Map. Used to generate
#                 hash code determining the entry's bucket in the Hash Map.
#                 This ensures that every entry can be efficiently located.

# Hash Code : A number generated from key, to determine what bucket that H.M entry belongs to.

# Bucket    : Hash Map consists of many such buckets, or containers, to store entries.

# Value     : Can be nearly any kind of information, like name, birth date, and address of a person.
#             The value can be many different kinds of information combined.


print("\033[95m\n{------------------------------")


class SimpleHashMap:
    def __init__(self, size=100):
        self.size = size
        self.bucket = [[] for char in range(size)]

    def hash_function(self, key):
        return sum(int(char) for char in key if char.isdigit()) % self.size


    def puts(self, key, value):
        index = self.hash_function(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # update existing key
                return

        bucket.append((key, value))  # add new key-value pair

    def get(self, key):
        index = self.hash_function(key)
        bucket = self.bucket[index]

        for i, (k, v) in enumerate(bucket):
            if k == key:
                return v
        return None

    def remove(self, key):
        index = self.hash_function(key)
        bucket = self.bucket[index]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return

    def print_map(self):
        print("hash map content:")
        for counter, value in enumerate(self.bucket):
            print(f" Index {counter}: {value}")


hash_map = SimpleHashMap(10)

hash_map.puts("763-343-3423", "hamza")
hash_map.puts("763-654-4645", "haider")
hash_map.puts("763-854-5545", "hashim")

hash_map.puts("753-674-4645", "ali")
hash_map.puts("763-684-5125", "alex")
hash_map.puts("733-654-5345", "mina")

hash_map.puts("763-654-5675", "elaina")
hash_map.puts("773-664-5675", "mikail")
hash_map.puts("723-654-5669", "hasan")
hash_map.puts("723-653-5657", "hussain")

hash_map.print_map()

print("name associate with '763-684-5125' is: ",hash_map.get("763-684-5125"))  
print("\n")
print(f"updating the name  for '763-654-4645' to  'john': ") 
hash_map.puts("763-654-4645","john")
print("new name associate with '763-654-4645' is : ", hash_map.get("763-654-4645"))




# A Hash Map is a data structure that stores key-value pairs and allows for efficient retrieval of values by their corresponding keys. 
# The class has the following methods:

# 1.  __init__(self, size=100)`: This is the constructor method that initializes the Hash Map
#       with a specified size (default is 100). It creates an empty list of lists (buckets) with the specified size.

# 2. `hash_function(self, key)`: This method takes a key as input and returns a hash code
#       based on the key. The hash code determines the bucket where the key-value pair
#       will be stored. In this implementation, the hash code is calculated by summing
#       the digits in the key and then modulo the size of the Hash Map.

# 3. `puts(self, key, value)`: This method adds a key-value pair to the Hash Map.
#       It first calculates the hash code for the key using the `hash_function` method.
#       Then, it checks if the key already exists in the bucket. If it does, it updates
#       the value for the key. Otherwise, it appends the new key-value pair to the bucket.
    
# 4. `get(self, key)`: This method retrieves the value for a given key from the Hash Map.
#     It first calculates the hash code for the key using the `hash_function` method.
#     Then, it iterates through the bucket and returns the value for the first key that
#     matches the input key. If no matching key is found, it returns `None`.

# Overall, this code provides a simple implementation of a Hash Map in Python.
#   It uses a list of lists to represent the buckets and a hash function to determine the
#    bucket for each key-value pair. The `puts` method adds new key-value pairs to the
#     Hash Map,    and the `get` method retrieves the value for a given key.

print("\n------------------------------}\n\033[0m")









