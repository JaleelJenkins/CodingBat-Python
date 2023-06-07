'''
Question 9 - not_string - Given a string, return a new string where "not " has been
added to the front. However, if the string already begins with "not", return the string
unchanged.

Expected Output:
`not_string('candy') → 'not candy'`
`not_string('x') → 'not x'`
`not_string('not bad') → 'not bad'`

'''
def not_string(str):
    # if the string already BEGINS with "not", return string unchanged.
    if str.startswith('not'):
        return str
    # returns a new string wehre "not" has been added to the front.
    else:
        return "not " + str

'''
Approach #2
    def not_string(str):
        if len(str) >= 3 and str[:3] == "not":
            return str
        return "not " + str

 Case Statements
    Case #1 - given a string, return a new string where "not" is added to the front.
    Case #2 - If string already begin with not just return the string.
    
    Need to make sure your checking the string for "not" first in conditional statement.

'''