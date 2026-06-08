class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        smal = []
        same = []
        big = []
        for i in range(len(nums)):
            if nums[i] >  pivot:
                big.append(nums[i])
            elif nums[i] <pivot:
                smal.append(nums[i])
            elif nums[i] == pivot:
                same.append(nums[i])
        return smal+same+big


