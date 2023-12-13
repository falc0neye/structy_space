def five_sort(nums):
    # set tail position to first occurance of 5
    # iterate through list and move non-5 elements to tail position
    # store as temp and set tail to current index
    tail = None
    for idx, el in enumerate(nums):
        print(idx, el)
        print(nums)
        # finds and sets initial tail position
        if el == 5 and tail == None:
            print('found first 5')
            tail = idx
            continue
        
        if el != 5 and tail != None:
            print(idx, el)
            temp = nums[idx] # stores temp value
            nums[idx] = nums[tail]
            nums[tail] = temp
            # tail = idx
            tail += 1
            continue
        
    return nums
        
        
print(five_sort([12, 5, 1, 5, 12, 7]))
# -> [12, 7, 1, 12, 5, 5] 