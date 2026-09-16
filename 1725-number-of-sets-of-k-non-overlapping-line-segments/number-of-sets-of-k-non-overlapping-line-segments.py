class Solution(object):
    def numberOfSets(self, n, k):
        memo = {}
        def qntd(a, b):
            if b == 0 or b == a:
                return 1
            if (a, b) in memo:
                return memo[(a, b)]
            memo[(a, b)] = qntd(a - 1, b - 1) + qntd(a - 1, b)
            return memo[(a, b)]

        return qntd(n + k - 1, 2 * k) % (10**9 + 7)