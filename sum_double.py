'''
Question 3 - sum_double - Given two int values, return their sum. Unless the two values
are the same, then return double their sum.

Expected Output:
`sum_double(1, 2) → 3`
`sum_double(3, 2) → 5`
`sum_double(2, 2) → 8`

'''
def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

'''
Approach #2 
    def sum_double(a, b):
        sum = a + b
        
        if a == b:
            sum = sum * 2
        return sum
        
Summary -
 In the problem statment we ar given 2 cases to deal with.
    Case #1 - Given two int values return their sum
    Case #2 - If they are the same in value the return double their sum
    
 Need to validate they are not the same first using an if, else. Logic being
 if they're equal in value return double their sum, else return their sum.        

'''