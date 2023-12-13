# Write a function, compress, that takes in a string as an argument. 
# The function should return a compressed version of the string 
# where consecutive occurrences of the same characters are 
# compressed into the number of occurrences followed by the character. 
# Single character occurrences should not be changed.
# 'aaa' compresses to '3a'
# 'cc' compresses to '2c'
# 't' should remain as 't'

def compress(s):
    tail = 0
    lead = 1
    o = ''
    # iterate over string
    # while lead is equal to tail, increment lead
    # when lead is not equal to tail, 
        # if diff in indicies = 1 then add char at tail index
        # else add diff between lead - tail and append char at tail index
    while (lead <= len(s)):
        if lead == len(s):
            if lead - tail == 1:
                o += s[tail]
                tail = lead
                lead += 1
                continue
            else:
                o += str(lead - tail) + s[tail]
                lead += 1
                continue
        print(s[tail])
        print(s[lead])
        if s[lead] == s[tail]:
            lead += 1
            continue
        if s[lead] != s[tail]:
            if lead - tail == 1:
                o += s[tail]
                tail = lead
                lead += 1
                continue
            else:
                o += str(lead - tail) + s[tail]
                tail = lead
                lead += 1
                continue
        lead += 1
        
        
    return o
        
# # print(compress('caat'))
# print(compress('ccaaatsss')) # -> '2c3at3s'
# print(compress('ssssbbz')) # -> '4s2bz')
# print(compress('ppoppppp')) # -> '2po5p')
# print(compress('nnneeeeeeeeeeeezz')) # -> '3n12e2z'
# -> '127y')