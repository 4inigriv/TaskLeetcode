class Solution(object):

    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        # "9+3+2+9=23 5+9+9+9=32"
        for i in range(half):  # ?329
            if num[i] == "?":
                left_q += 1  # 1
            else:
                left_sum += int(num[i])  # 3 + 2 + 9 = 14

        # metade direita
        for i in range(half, n):
            if num[i] == "?":
                right_q += 1  # 3
            else:
                right_sum += int(num[i])  # 5???

        todes = left_q + right_q
        if todes % 2 == 0: #é par?
            if 9 * ((left_q - right_q) // 2) + (left_sum - right_sum) != 0:
                return True
            return False
        return True
            


