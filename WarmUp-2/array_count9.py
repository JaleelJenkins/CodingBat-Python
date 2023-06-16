'''
array_count9 - Given an array of ints, return the number of 9's in the array.

Expected Output:
array_count9([1, 2, 9]) → 1
array_count9([1, 9, 9]) → 2
array_count9([1, 9, 9, 3, 9]) → 3

'''
def array_count9(nums):
    ttl_cnt = 0

    for num in nums:
        if num == 9:
            ttl_cnt += 1
    return ttl_cnt

'''
Approach Breakdown
    -- Create count variable to store final count
    -- Loop through array 
    -- Set a check for numerical value == 9
    -- Increment count to end of the loop
    -- Return the value 
    
Big Idea: Looping through an array and inspecting every elements
    
    FOR LOOP
      IF
    
  nums = [1, 2, 9]
  
  nums[0] == 9 --> 1 == 9 --> FALSE 
  nums[1] == 9 --> 2 == 9 --> FALSE 
  nums[2] == 9 --> 9 == 9 --> TRUE --> CTR = CTR + 1

'''