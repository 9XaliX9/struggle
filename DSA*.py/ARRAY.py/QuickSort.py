print("\033[95m\n------------------------------")

# QUICK SORT
# How it works:

# Choose a value in array to be the pivot element.
# Order rest of the array so that lower values than pivot element are on left, and higher values are on right.
# Swap pivot element with first element of higher values so that pivot element lands in between lower and higher values.
# Do same operations (recursively) for sub-arrays on the left and right side of pivot element.

def partition(array, low, high):
    pivot = array[high]
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksort(array, low=0, high=None):
    if high is None:
        high = len(array) - 1

    if low < high:
        pivot_index = partition(array, low, high)
        quicksort(array, low, pivot_index - 1)
        quicksort(array, pivot_index + 1, high)

my_array = [64, 34, 25, 12, 22, 11, 90, 5]
quicksort(my_array)
print("Sorted array:", my_array)

print("\n------------------------------\n\033[0m")
