'''
first_last6 - Given an array of ints, return True if 6 appears as
either the first or last element in the array. The array will be
length 1 or more.

Expected Output:
first_last6([1, 2, 6]) → True
first_last6([6, 1, 2, 3]) → True
first_last6([13, 6, 1, 2, 3]) → False

'''
def fist_last6(nums):
    return (nums[0] == 6 or nums[-1] == 6)

'''
        0 1 2
nums = [1,2,6]

#Good practice always pull the length as a variable

    x = len(nums) #gets the length of nums
    
    if (nums[0] == 6 or nums[x - 1] == 6):
        return True
    
    return False 
'''