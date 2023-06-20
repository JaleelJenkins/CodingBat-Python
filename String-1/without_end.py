'''
without_end - Given a string, return a version without the first and
last char, so "Hello" yields "ell". The string length will be at
least 2.

Expected Output:
without_end('Hello') → 'ell'
without_end('java') → 'av'
without_end('coding') → 'odin'

'''
def withou_end(str):
    return str[1:len(str) - 1]