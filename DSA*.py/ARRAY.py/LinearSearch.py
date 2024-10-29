print("\033[95m\n------------------------------")
# LINEAR SEARCH ALGORITHM

# How it works:

# Go through array value by value from the start.
# Compare each value to check if is equal to the value we are looking for.
# If the value found, return the index of that value.
# If the end of array is reached and the value is not found, return -1 to indicate that value not found.


def Linear(num, target_value):
    for i in range(len(num)):
        if num[i] == target_value:
            return i
    return -1

num = [2, 4, 6, 7, 8, 9]
target_value = 8

result = Linear(num, target_value)

if result != -1:
    print("found at:", result)
else:
    print("not found.")

print("\n------------------------------\n\033[0m")
