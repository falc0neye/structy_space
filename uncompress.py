# Write a function, uncompress, that takes in a string as an argument. 
# The input string will be formatted into 
# multiple groups according to the following pattern:
# <number><char>
# for example, '2c' or '3a'.
# uncompress("2c3a1t") # -> 'ccaaat'

# print(int('1'))

def uncompress(s):
  
  repeatTimes = ''
  returnStr = ''
  
  for char in s: 
    # if char is not a number, store in temp and continue
    # else update return string adding char and repeating N times
    if char.isnumeric():
      repeatTimes += char
      continue
    else:
      returnStr += char*int(repeatTimes)
      repeatTimes = ''
  
  return returnStr



print(uncompress('10c3a1t'))

