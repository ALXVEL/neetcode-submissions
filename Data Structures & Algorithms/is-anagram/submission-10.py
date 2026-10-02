class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s = s.lower()
        t = t.lower()

        s_dict = {}
        t_dict = {}

        if len(s) != len(t):
            return False

        for i in range(0, len(s)):
            s_dict[s[i]] = 1 + s_dict.get(s[i], 0)
            t_dict[t[i]] = 1 + t_dict.get(t[i], 0)
        
        return s_dict == t_dict
        