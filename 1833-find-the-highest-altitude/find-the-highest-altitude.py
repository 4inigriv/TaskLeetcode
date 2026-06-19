class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        altitude = 0
        maior = 0
        for i in range(len(gain)):
            altitude += gain[i]
            if altitude > maior:
                maior = altitude
        return maior

