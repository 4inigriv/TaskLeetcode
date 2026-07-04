
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        seq = {}
        for i in text:
            if i in seq:
                seq[i] +=1
            else:
                seq[i] = 1 
        if 'l' in seq:
            seq['l'] //= 2     
        if 'o' in seq:
            seq['o'] //= 2

        return min(
            seq.get('b',0),
            seq.get('a',0),
            seq.get('l',0),
            seq.get('o',0),
            seq.get('n',0)
        )