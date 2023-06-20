'''
end_other - Given two strings, return True if either of the strings appears at the very end of the other string,
ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
Note: s.lower() returns the lowercase version of a string.

Expected Output:
end_other('Hiabc', 'abc') → True
end_other('AbC', 'HiaBc') → True
end_other('abc', 'abXabc') → True

'''
def end_other(a, b):
    a = a.lower()
    b = b.lower()

    lstr = a
    sstr = b

    if len( b ) > len( a ):
        lstr = b
        sstr = a

    if sstr == lstr[len( lstr ) - len( sstr ): len( lstr )]:
        return True
    return False

'''
  # a = 'Hiabc', b = 'abc'
  #
  # Convert to lowercase and establish large and small
  #          01234
  # large = "hiabc"
  # small = "abc"
  
  # check = large[2:5] --> large[len(large) - len(small) : len(large)]
  
  
  # if check == small return True
  
  #How to generalize substring base on lenght of small and large

'''
