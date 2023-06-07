'''
Question 6 - make10 - Give 2 ints, a and b, return True if one of them is 10 or their sum
is 10.

Expected Output:
`makes10(9, 10) → True`
`makes10(9, 9) → False`
`makes10(1, 9) → True`

'''
def makes10(a, b):
    return (a + b == 10) or (a == 10 or b == 10)

'''
Approach #2 
    def makes10(a, b):
        return (a == 10 or b == 10 or a+b == 10)
'''