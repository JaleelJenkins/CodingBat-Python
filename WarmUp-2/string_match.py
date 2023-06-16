'''
string_match - Given 2 strings, a and b, return the number of the positions where
they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3,
since the "xx", "aa", and "az" substrings appear in the same place in both strings.

Expected Output:
string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0

'''
def string_match(a, b):
    min_len = min(len(a), len(b))
    ctr = 0

    for i in range(0, min_len - 1, 1):
        if (a[i:i + 2] == b[i:i + 2]):
            ctr = ctr + 1

    return ctr

'''
Approach Breakdown 
  Big Idea 1: Picking smaller string to set loop length
  Big Idea 2: Since the reading frame is 2 characters setting the loop length
              so that the loop counter stops at the second last index
       0123456
  a = 'xxcaazz'
       012345
  b = 'xxbaaz'  <-- smaller length so this drives our loop parameters

  012345
  xxbaaz
  XX

  Big Idea 3: We have to run full loop before exiting so there is NO return
  statement in the loop
'''