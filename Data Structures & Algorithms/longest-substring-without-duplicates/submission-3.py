class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        L = 0
        maxLen = 0

        for R in range(0, len(s)):        
            while(s[R] in s[L:R]):
                L+=1
            maxLen = max(maxLen, R-L+1)
            print(f'R: {R}  L: {L}')
        
        return maxLen