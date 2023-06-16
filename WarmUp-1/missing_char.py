'''
Question 10 - missing_char - Given a non-empty string and an int n, return a new string
where the char at index n has been removed. The value of n will be a valid index of
a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

Expected Output:
missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'

'''
def missing_char(str, n):
    modified_str = ""

    for char in range(0, len(str)):
        if (char != n):
            modified_str += str[char]

    return modified_str
