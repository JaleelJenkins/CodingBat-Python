'''
double_char - Given a string, return a string where for every char in the original, there are two chars.

Expected Output:
double_char('The') → 'TThhee'
double_char('AAbb') → 'AAAAbbbb'
double_char('Hi-There') → 'HHii--TThheerree'

'''
def dobule_char(str):
    result = ""

    for i in range(0, len(str), 1):
        result = result + str[i] + str[i]

    return result


'''
for i in range(0, len(str), 1): 
  <CODE BLOCK>

      012
str = The l = 3

i = 0       0 < 3 TRUE - RUN LOOP
  newStr = "TT"
i = 1       1 < 3 TRUE - RUN LOOP
  newStr = "TT" + "hh"
i = 2       2 < 3 TRUE - RUN LOOP
  newStr = "TThh" + "ee"
i = 3       3 < 3 FALSE EXIT LOOP
'''