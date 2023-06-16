'''
array_front9 - Given an array of ints, return True if one of the first 4 elements in the
array is a 9. The array length may be less than 4.

Expected Output:
array_front9([1, 2, 9, 3, 4]) → True
array_front9([1, 2, 3, 4, 9]) → False
array_front9([1, 2, 3, 4, 5]) → False

'''
def array_front9(nums):
    for i in nums[:4]:
        if i == 9:
            return True
    return False

'''
Approach Breakdown 
  Two Big Things
  1.  The function can exit as soon as a 9 is found!
  2.  We only want to loop through the first four elements, or if the list 
      is smaller just the length
      
Quickest Approach 
    
    return 9 in nums[0:4]
    
'''