""" Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0] """

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i,num in enumerate(nums):
            if(i == len(nums)-1):
                break
            else:
                next = nums[i+1]
            
            if num == 0 and next != 0:
                nums.pop(i)
                nums.append(num)
            elif num == next == 0:
                nums.pop(i)
                nums.remove(next)
                nums.append(0)
                nums.append(0)

s = Solution()
s.moveZeroes([0])



# optimal solution

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        non_zero = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero],nums[i] = nums[i], nums[non_zero]
                non_zero += 1

        print(nums)



s = Solution()
s.moveZeroes([0,1,2,0,0,0,12])