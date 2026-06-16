class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        repeat = len(nums)//2
        element = 0
        dic = {}
        for i in range(len(nums)):
            element = nums[i]
            if element in dic:
                dic[element]+=1
            else:
                dic[element]=1
            if dic[element] > repeat:
                return element
     