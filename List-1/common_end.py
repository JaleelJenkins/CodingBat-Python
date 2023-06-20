'''
common_end - Given 2 array of ints, a and b, return True if they have
the same first element or they have the same last element. Both
arrays will be length 1 or more.

Expected Output:
common_end([1, 2, 3], [7, 3]) → True
common_end([1, 2, 3], [7, 3, 2]) → False
common_end([1, 2, 3], [1, 3]) → True

'''
def common_end(a, b):
    return (a[0] == b[0] or a[-1] == b[-1])

'''
#Technique: Since the boolean expression returns True we can simple return
the boolean expressions
'''