'''
reverse3 - Given an array on ints length 3, return a new array with the elements
in reverse order, so {1, 2, 3}  becomes {3, 2, 1}.

Expected Output:
reverse3([1, 2, 3]) → [3, 2, 1]
reverse3([5, 11, 9]) → [9, 11, 5]
reverse3([7, 0, 0]) → [0, 0, 7]

'''
def reverse3(nums):
    nums.reverse()
    return nums

'''
Different Approach: Make a new list
nums1 = [nums[2], nums[1], nums[0]]
return nums1

As a Oneliner approach 
return [nums[2], nums[1], nums[0]]

'''
