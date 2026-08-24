class Solution(object):
    def canWinNim(self, n):
        if n == 1:
            return True #pq começo primeiro ent venço
        if n % 4 != 0:
            return True #eu ganho qnd n é multiplo de 4
        else:
            return False
            

        