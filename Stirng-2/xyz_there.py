'''
xyz_there - Return True if the given string contains an appearance of "xyz" where the xyz is not directly preceeded
by a period (.). So "xxyz" counts but "x.xyz" does not.

Expected Output:
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True

'''
def xyz_there(str):
    for i in range(0, len(str) -2, 1):
        if str[i:i+3] == "xyz" and str[i - 1] != ".":
            return True

    return False

'''
  #Approach 2:
  #
  # Fun one-liner that is a nice practice in stringing together function calls
  
  #
  # str = abc.xyzxyz
  # str.replace(".xyz") --> abcxyz
  #
  
  #return str.find("xyz") >= 0 and str.find(".xyz") == -1
  #return  str.replace(".xyz","").find("xyz") >= 0
  
  #Notice that in this problem we can simply return when we find what 
  #we need
  
  #Approach 3
  #Check first three
  #       0123456789
  # str = abc.xyzxyz
  #       XiXX

'''