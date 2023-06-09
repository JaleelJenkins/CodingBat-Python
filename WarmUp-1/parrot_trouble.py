'''
Question 5 - parrot_trouble - We have a loud talking parrot. The "hour" parameter is
the current hour time in the range 0..23. We are in trouble if the parrot is talking
and the hour is before 7 or after 20. Return True if we are in trouble.

Expected Output:
`parrot_trouble(True, 6) → True`
`parrot_trouble(True, 7) → False`
`parrot_trouble(False, 6) → False`

'''
def parrot_trouble(talking, hour):
    if (hour < 7 or hour > 20) and talking == True:
        return True
    else:
        return False

'''
Approach #2 
    def parrot_trouble(talking, hour):
        return (talking and (hour < 7 or hour > 20))

Case Statements 
    Case #1 - We are in trouble if the parrot is talking and the hour is before 7 or 
    after 20.
    
 We can use just an if statment to validate this case. Make sure to use parathesis
 around the OR clause since the AND clause binds more tightly than or.
'''