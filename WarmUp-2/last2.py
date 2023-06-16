'''
last2 - Given a string, return the count of the number of times that a substring length 2
appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1
(we won't count the end substring).

Expected Output:
last2('hixxhi') → 1
last2('xaxxaxaxx') → 1
last2('axxxaaxx') → 2

'''
def last2(str):
    cnt = 0
    tempStr = str[len(str) -  2: len(str)]

    for i in range(0, len(str) - 2, 1):
        if str[i:i+2] == tempStr:
            cnt += 1

    return cnt

'''
Approach Breakdown 
    -- This is an essential concept. We need to be able to count the number of times a 
    specific instance appears in the string.
    
    012345
    hixxhi
        hi
    
    "hi" == str[0:2] --> True 
    "hi" == str[1:3] --> False
    "hi" == str[2:4] --> False
    "hi" == str[3:5] --> False 

'''