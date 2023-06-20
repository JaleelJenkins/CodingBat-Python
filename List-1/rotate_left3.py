'''
rotate_left3 - Given an array of ints length 3, return an array with
the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.

Expected Output:
rotate_left3([1, 2, 3]) → [2, 3, 1]
rotate_left3([5, 11, 9]) → [11, 9, 5]
rotate_left3([7, 0, 0]) → [0, 0, 7]

'''
def rotate_left3(nums):
    return [nums[1], nums[2], nums[0]]

'''
List are reference variables.

#New Line: Save nums[0] in a temp variable before we write over it
temp = nums[0]
#Current State nums = [1,2,3] - WE LOSE nums[0]
nums[0] = nums[1]
#Current State nums = [2,2,3]
nums[1] = nums[2]
#Current State nums = [2,3,3]
nums[2] = temp #change this to copy temp into nums[2]
#Current State nums = [2,3,2]
return nums

'''