# Write a function, most_frequent_char, that takes in a string as an argument. 
# The function should return the most frequent character of the string. 
# If there are ties, return the character that appears earlier in the string.
# You can assume that the input string is non-empty.

def most_frequent_char(s):
    cache = {
        'currentMax': float('-inf'),
        'currentChar': '',
    }
    for idx, char in enumerate(s):
        print(idx, char)
        print(cache['currentMax'])
        print(cache['currentChar'])
        if char not in cache:
            cache[char] = {
                'value': 1,
                'idx': idx
            }
        else:
            cache[char]['value'] += 1
        print(cache[char]['value'])
        print(cache['currentMax'])
        print(char)
        if cache[char]['value'] > cache['currentMax']:
            cache['currentMax'] = cache[char]['value']
            cache['currentChar'] = char
        if cache[char]['value'] == cache['currentMax'] and cache[char]['idx'] < cache[cache['currentChar']]['idx']:
            cache['currentMax'] = cache[char]['value']
            cache['currentChar'] = char

    # print(cache)
    return cache['currentChar']

print(most_frequent_char('mississippi'))