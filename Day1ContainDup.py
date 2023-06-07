# Remove Duplicates from Sorted Array

# """
#     Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such
# """
class Solution:
    def duplicate(self, nums):
        take = 0
        Solution.Sort(nums)
        for i in range(0 , len(nums) - 1):
            take +=1
            if nums[i] == nums[i + 1]:
                return True, nums, take

        return False, nums, take,
    
    def Sort(nums):
        LENGTH = len(nums)
        count = 0
        while True:
            if count < LENGTH - 1:
                if nums[count] > nums[count + 1]:
                    pHolder = nums[count]
                    nums[count] = nums[count + 1]
                    nums[count + 1] = pHolder
            elif LENGTH < 1:
                break
            else:
                count = 0
                LENGTH -= 1
            count+=1
        
        return nums
