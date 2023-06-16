'''
Question 4 - diff21 - Given an int n, return the absolute difference between n and 21,
except return double the absolute difference if n is over 21.

Expected Output:
`diff21(19) → 2`
`diff21(10) → 11`
`diff21(21) → 0`

'''
def diff221(n):
    if n < 21:
        x = abs(n - 21)
    else:
        x = abs(n -21) * 2
    return x

'''
Approach #2
    def diff21(n):
        if n <= 21:
            return 21 - n
        else:
            return (n - 21) * 2

Summary -
 Case #1 - return absolute difference of a given int and 21
 Case #2 - if int is over 21 return double the absolute difference 

'''