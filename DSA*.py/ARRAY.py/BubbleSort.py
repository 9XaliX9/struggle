print("\033[95m\n------------------------------")

#BUBBLE SORT
# How it works:

# Go through the array, one value at a time.
# For each value, compare value with the next value.
# If value is higher than next one, swap values so highest value comes last.
# Go through array as many times as there are values in array.

my_array = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(my_array)
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j] > my_array[j+1]:
            my_array[j], my_array[j+1] = my_array[j+1], my_array[j]

print("Sorted array:", my_array)

print("\n------------------------------\n\033[0m")
