class Solution(object):
    def climbStairs(self, n):
        qntd = 0
        jasubidas = {}
        def memo(n):
            if n in jasubidas:
                return jasubidas[n]
            if n == 1:
                return 1
            if n == 2:
                return 2
            jasubidas[n] = memo(n-1) + memo(n-2)
            return jasubidas[n]
        return memo(n) #chama a funçao        
        