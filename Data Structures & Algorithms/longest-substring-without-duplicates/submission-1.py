class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        l = 0
        freq = set()
        for r in range(len(s)):
            while s[r] in freq:
                freq.remove(s[l])
                l+=1          
            freq.add(s[r])
            res= max(res, r-l+1)
        return res




        