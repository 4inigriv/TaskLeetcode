'''
1-> sum leftsum -> 
2-> sum rightsum

answer = left - right
'''
class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        acumulateleft = 0
        acumulateright =0
        leftsum = 0
        rightsum = 0
        listsuml= []
        listsumr = []
        for i in range(len(nums)):
            listsuml.append(acumulateleft) #first elemento its 0 so append BEFORE sum
            acumulateleft += nums[i] #sum acumulate of leftsum
        for i in range(len(nums)-1,-1,-1): 
            listsumr.append(acumulateright)
            acumulateright += nums[i] #sum acumulate of rightsum
        listsumr = listsumr[::-1] #reverse
        r = []
        for i in range(len(nums)):
            if listsuml[i] >= listsumr[i]:
                ans = listsuml[i]-listsumr[i]
            else:
                ans = listsumr[i]-listsuml[i]
            r.append(ans)
        return r
'''
TIME: O(N+M+K) -> O(n)
SPACE: O(n) -> criei 2 listas diferentes 

'''