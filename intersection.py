# Write a function, intersection, that takes in two lists, a,b, as arguments. 
# The function should return a new list containing elements that are in both of the two lists.
# You may assume that each input list does not contain duplicate elements.

def intersection(a, b):
    # while each list has length, pop elements and add to cache
    # after adding to cache, check if count is = 2 and if so, push to return list
    cache = {}
    return_list = []
    while len(a) > 0 or len(b) > 0:
        if len(a) > 0:
            temp_a = a.pop()
            if temp_a not in cache:
                cache[temp_a] = 1
            else:
                cache[temp_a] += 1
        
            if cache[temp_a] == 2:
                return_list.append(temp_a)

        if len(b) > 0:
            temp_b = b.pop()
            if temp_b not in cache:
                cache[temp_b] = 1
            else:
                cache[temp_b] += 1
            if cache[temp_b] == 2:
                return_list.append(temp_b)
    return return_list



#print(intersection([4,2,1,6], [3,6,9,2,10])) # -> [2,6]
# intersection([2,4,6], [4,2]) # -> [2,4]
# intersection([4,2,1], [1,2,4,6]) # -> [1,2,4]
print(intersection([0,1,2], [10,11])) # -> [])