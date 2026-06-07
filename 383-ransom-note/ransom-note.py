class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        list_magazine = list(magazine)
        for ch in ransomNote:
            if ch in list_magazine:
                list_magazine.remove(ch)
            else:
                return False
        return True