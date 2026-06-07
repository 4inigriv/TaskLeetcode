class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            element = nums.pop(i)
            crescent = True
            for j in range(len(nums)-1):
                if nums[j] >= nums[j+1]:
                    crescent = False
                    break
            nums.insert(i,element)

            if crescent == True:
                return True
        return False 


  
 