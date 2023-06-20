'''
cont_hi - Return the number of times that the string "hi" appears anywhere in the given string.

Expected Output:
count_hi('abc hi ho') → 1
count_hi('ABChi hi') → 2
count_hi('hihi') → 2

'''
def count_hi(str):
    cnt = 0

    for i in range(0, len(str) - 1, 1):
        temp = str[i:i + 2]
        if temp == "hi":
            cnt += 1
        return cnt

'''
  #Approach 2: Learn Reading Frames
  #Reading Frames
  #
  # Looking for the word "hi" that means I need to look at two letters at 
  # a time
  #
  # 012345678
  # abc hi ho
  # XX     XX
  #
  # str[0:2] substring is inclusive:exclusive
  # str[7:9]
  #
  #
  #
  
    Approach #3
    return str.count("hi")
'''