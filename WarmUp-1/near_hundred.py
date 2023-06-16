'''
Question 7 - near_hundred - Given an int n, return True if it is within 10 of 100 or 200.
Note: abs(num) computes the absolute value of a number.

Expected Output:
`near_hundred(93) → True`
`near_hundred(90) → True`
`near_hundred(89) → False`

'''
def near_hundred(n):
    # Reminder: Range is up too the second number. So up too 111 still counting 110.
    return (n in range(90, 111) or n in range(190, 211))

'''
Approach #2
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    
range(start, stop[, step])
    start: is the starting number of the sequence.
    stop: is the ending number of the sequence. If stop is not specified, it defaults to 
        None, which means the sequence will extend to infinity.
    step: is the step size. If step is not specified, it defaults to 1.
'''