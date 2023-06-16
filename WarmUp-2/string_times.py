'''
string_times - Given a string and a non-negative int n, return a larger string that
is n copies of the original string.

Expected Output:
string_times('Hi', 2) → 'HiHi'
string_times('Hi', 3) → 'HiHiHi'
string_times('Hi', 1) → 'Hi'

'''
def string_times(str, n):
    if n > -1:
        return str * n

'''
Approach Breakdown
    -- Do we need to do a validation on the int coming in to check if it is positive
    -- return string * n
    
Approach #2
 -- This question highlights two essential ideas.
    - String Construction
    - Loops

    tstr = ""
    for i in range(0,n,1):
        tstr = tstr + tstr 
    
    return tstr
  

Approach #3
 -- A while loop is a conditional loop. While loops and for loops 
 are interchangeable.
 
    tstr = ""
    i = 0;
    while (i < n):
        tstr = tstr + str
        i = i + 1
    return tstr
'''
