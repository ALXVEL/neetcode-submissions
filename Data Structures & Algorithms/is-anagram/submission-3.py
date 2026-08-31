class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}

        if len(t) != len(s):
            return False 

        if len(set(t)) != len(set(s)):
            return False

        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 0
        
        for i in t:
            if i in t_dict:
                t_dict[i] += 1
            else:
                t_dict[i] = 0
        
        for key, value in s_dict.items():
            if key in t_dict.keys():
                if s_dict[key] != t_dict[key]:
                    return False
            else:
                return False

        return True 
        