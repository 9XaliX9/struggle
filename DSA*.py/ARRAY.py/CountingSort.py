
print("\033[95m\n------------------------------")

# How it works:
#COUNTING

# Create new array for counting how many there are of the different values.
# Go through the array that needs to be sorted.
# For each value, count by increasing counting array at the corresponding index.
# After counting values, go through counting array to create the sorted array.
# For each count in counting array, create correct number of elements,
#     with values that correspond to counting array index.


def countingSort(arr):
    max_val = max(arr)
    count = [0] * (max_val + 1)

    while len(arr) > 0:
        num = arr.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            arr.append(i)
            count[i] -= 1

    return arr

unsortedArr = [4, 2, 2, 6, 3, 3, 1, 6, 5, 2, 3]
sortedArr = countingSort(unsortedArr)
print("Sorted array:", sortedArr)

print("\n------------------------------\n\033[0m")

