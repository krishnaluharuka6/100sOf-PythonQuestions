# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.You may assume that each input would have exactly one solution, and you may not use the same element twice.

def twoSum(nums, target):
        for a in range(0,len(nums)):
            for b in range(a+1,len(nums)):
                if nums[a] + nums[b] == target:
                    return [a,b]


result=twoSum([3,2,4], 6)
print(result)



# optimal solution
def sum(nums, target):
    self = {}
    for i,num in enumerate(nums):
        complement = target - num
        if complement in self:
            return [self[complement],i]
        self[num] = i

result = sum([3,4,3],6)
print(result)
          

