def pair_sum(numbers, target_sum):
    # create set to store diffs
    cache = {}
    # iterate through list and look for matching diff
    # if not exists add to Set
    # if exists return 
    for idx, el in enumerate(numbers):

        diff = target_sum - el
        if el in cache:
            print('in cache')
            return (cache[el]['index'], idx)
        else:
            cache[diff] = {
                'value': el,
                'index': idx
            }
    return None

print(pair_sum([3, 2, 5, 4, 1], 8))  # -> (0, 2)