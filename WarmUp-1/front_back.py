'''
Question 11 - front_back - Given a string, return a new string where the first and last
chars have been exchanged.

Expected Output:
front_back('code') → 'eodc'
front_back('a') → 'a'
front_back('ab') → 'ba'

'''
def front_back(str):
    if len(str) > 1:
        front = str[:1]
        back = str[-1:]
        body = str[1:-1]
    else:
        return str

    return back + body + front

'''
Approach -
    -- Slice the string by first character and save it to a variable 
    -- Same for the last string
    -- Same for the body of the string
    -- Concatenate them all together

Summary -
 Case #1 - return absolute difference of a given int and 21
 Case #2 - if int is over 21 return double the absolute difference 

'''