class Solution(object):
    def missingMultiple(self, nums, k):
        nums_set = set(nums)
        bigger = k
        while bigger in nums_set:
            if bigger % k == 0:
                bigger +=k
                if bigger not in nums_set:
                    break
        
        return bigger 