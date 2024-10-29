print("\033[95m\n------------------------------")
# BINARY SEARCH ALGORITHM

# How it works:
# Check the value in the center of the array.

# If the target value is lower, search the left half of the array.
#    If the target value is higher, search the right half.

# Continue step 1 and 2 for the new reduced part of the array until 
#   the target value is found or until the search area is empty.

# If the value is found, return the target value index. If the target 
#   value is not found, return -1.
                                        
def binary(num_sorted,target_value):

    left =0
    right = len(num_sorted) -1

    while left<=right:
        mid = (left+right)//2

        if num_sorted[mid] ==target_value:
            return mid
        if num_sorted[mid] <target_value:
            left = mid +1
        else :
            right =mid-1

    return -1
target_value =67

num = [23,4,23,5,6,57,6,7,67,3,45,23,4,23,53,4,67]

num_sorted = sorted(num)
num_sorted_set = sorted(set(num))

result = binary(num_sorted,target_value)
result_set = binary(num_sorted_set,target_value)


print("target value:",target_value)
print(num_sorted)

if result != -1:
    print("found at index:",result)
else:
    print("not found.")


print(num_sorted_set)

if result_set != -1:
    print("found at index:",result_set)
else:
    print("not found.")

print("found at:",num_sorted.index(67))

                                        
print("\n------------------------------\n\033[0m")
