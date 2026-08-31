class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        char_s = {}
        char_t = {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            char_s[s[i]] = char_s.get(s[i], 0) + 1
            char_t[t[i]] = char_t.get(t[i], 0) + 1
        
        return char_s == char_t