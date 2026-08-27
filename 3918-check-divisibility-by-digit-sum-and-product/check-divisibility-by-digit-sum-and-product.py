class Solution(object):
    def checkDivisibility(self, n):
        s = 0
        prod = 1
        user = n
        while user > 0:
            rest = user % 10 #o ultimo elento
            s += rest
            prod *= rest  
            user //= 10 
        if n % (s+prod)==0: #n is divisible by the sum of the sum and prod
            return True
        else:
            return False