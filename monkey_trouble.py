'''
Question 2 - monkey_trouble - We have two monkeys, a and b, and the parameters a_smile
and b_smile indicate if each is smiling. We are in trouble if they are both smiling or
if neither of them is smiling. Return True if we are in trouble.

Expected Output:
`monkey_trouble(True, True) → True`
`monkey_trouble(False, False) → True`
`monkey_trouble(True, False) → False`

'''
def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and b_smile:
        return True
    return False

'''
Aproach #2 -
    return ((a_smile and b_smile) or (not a_smile and not b_smile))
    
Approach #3 - 
    return (a_smile == b_smile)
    

Summary -
 We use a simple if statement to directly check for each case.
    Case #1 - both monkeys smiling == Trouble
    Case #2 - both monkeys are not smiling == Trouble

'''