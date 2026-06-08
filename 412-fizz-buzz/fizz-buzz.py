class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1,n+1):
            if i % 5 == 0 and i % 3 == 0 : #divisible by 5 and 3
                ans.append("FizzBuzz")
            elif i % 3 == 0: #divisible by 3
                ans.append("Fizz")
            elif i % 5==0:# divisible by 5
                ans.append("Buzz")
            else:
                ans.append(str(i))
 

        return ans