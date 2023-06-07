'''
Question 8 - pos_neg - Given 2 int values, return True if one is negative and one is
positive. Except if the parameter "negative" is True, then return True only if both
are negative.

Expected Output:
`pos_neg(1, -1, False) → True`
`pos_neg(-1, 1, False) → True`
`pos_neg(-4, -5, True) → True`

'''
def pos_neg(a, b, negative):
    if (a < 0 and b < 0) and negative == True:
        return True
    elif negative == True:
        return False
    elif (a < 0 and b > 0) or (a > 0 and b < 0):
        return True
    else:
        return False

'''
Approach #2
    def pos_neg(a, b, negative):
        if negative:
            return (a < 0 and b < 0)
        else:
            return ((a < 0 and b > 0) or (a > 0 and b < 0))
            
Case Statements
    Case #1 - Return True if one is neg and one pos
    Case # 2 - If negative then only true if both are negative
    
 Build you cases from the bottom layer down.

'''