class Solution:
    def scoreOfString(self, s: str) -> int:

        total, prvNumOrd = 0, ord(s[0])

        for i in range(1,len(s)):
            total += abs(ord(s[i]) - prvNumOrd)
            prvNumOrd = ord(s[i])
        
        return total
        