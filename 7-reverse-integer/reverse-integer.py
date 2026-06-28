class Solution:
    def reverse(self, x: int) -> int:
        inverse = 0
        sinal = 1

        if x < 0:
            sinal = -1
            x = -x

        while x > 0:
            last = x % 10
            inverse = inverse * 10 + last
            x //= 10

        inverse = inverse * sinal

        if inverse < -2**31 or inverse > 2**31 - 1:
            return 0

        return inverse