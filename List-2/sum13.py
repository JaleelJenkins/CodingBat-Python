'''
sum13 - Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very
unlucky, so it does not count and numbers that come immediately after a 13 also do not count.

Expected Output:
sum13([1, 2, 2, 1]) → 6
sum13([1, 1]) → 2
sum13([1, 2, 2, 1, 13]) → 6

'''
def sum13(nums):
    if len(nums) == 0:
        return 0

    sum = 0
    i = 0

    while (i < len(nums)):
        if nums[i] == 13:
            nums.remove(nums[i])

            if i < len(nums):
                nums.remove(nums[i])

        if (i < len(nums) and nums[i] != 13):
            sum = sum + nums[i]
        i = i + 1
    return sum

  #
  #         0  1   2  3  4  5
  # nums = [1, 13, 2, 2, 1, 13]  --> 1 + 2 + 1 = 4
  #
  # i = 0    0 < 6 TRUE - RUN LOOP
  #     nums[0] != 13 TRUE
  #         sum = 1
  #
  # i = 1    1 < 6 TRUE - RUN LOOP
  #     nums[0] != 13 FALSE
  #         i = i + 1 = 2
  #
  # i = 3    3 < 6 TRUE - RUN LOOP
  #     nums[3] != 13 TRUE
  #       sum = 1 + 2 = 3
  #
  # i = 4    4 < 6 TRUE - RUN LOOP
  #     nums[4] != 13 TRUE
  #       sum = 3 + 1 = 4
  #
  # i = 5    5 < 6 TRUE - RUN LOOP
  #
  #     nums[5] != 13 FALSE
  #       i = i + 1 = 5 + 1 = 6
  #
  # i = 7    7 < 6 FALSE EXIT LOOP
  #
  # I am first going to write this using a for loop.  In Java this would
  # work perfectly.  In Python it does not! This is an important idea.
