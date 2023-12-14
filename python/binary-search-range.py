# Implement a function to search for an element in a sorted array.  
# The implementation should use the binary search algorithm 

# After you find number, store as current smallest/largest
# can be used to solve realistic problems
import math

def binary_search_range(nums, target):
    left = 0 # left index of binary search
    right = len(nums) - 1 # right index of binary seach
    # iterate and cut binary search in half depending on evaluation of current number compared to target
    while left <= right:
        print(left)
        print(right)
        # pointer is always equal to the midway point between left and right index positions
        pointer = math.floor((left + right) / 2) 
        print(pointer)
        # return index of match
        if nums[pointer] == target:
            return pointer #
        # if number at current pointer is > target, split array to left side
        elif nums[pointer] > target:
            right = pointer - 1
        else:
        # split array to right side since current pointer is < target
            left = pointer + 1
            
    return None

l = [1, 2, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 11]
#    0  1  2  3  4  5  6  7  8  9  10  11 12

# print(binary_search_sorted(l, 3)) # [2, 4]





