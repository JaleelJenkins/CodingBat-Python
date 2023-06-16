'''
stirng_splosion - Given a non-empty string like "Code" return a string like "CCoCodCode".

Expected Ouptut:
string_splosion('Code') → 'CCoCodCode'
string_splosion('abc') → 'aababc'
string_splosion('ab') → 'aab

'''
def stirng_splosion(str):
    result = ""

    for i in range(0, len(str) + 1, 1):
        result = result + str[0:i]

    return result

'''
Approach Breakdown 
    -- We will write a loop to move through each index and take the substring from 0
    to the loop counter. Watch we need to increase the loop counter by 1 to get the
    whole string added.
'''