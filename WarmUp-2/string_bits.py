'''
string_bits - Given a string, return a new string made of every other char starting with
the first, so "Hello" yields "Hlo".

Expected Output:
string_bits('Hello') → 'Hlo'
string_bits('Hi') → 'H'
string_bits('Heeololeo') → 'Hello'

'''
def string_bits(str):
    return str[::2]

'''
Approach Breakdown
    -- Create a new empty string.
    -- Loop through given string and find a way to store every other character to the new string.
    -- Return new string.
'''