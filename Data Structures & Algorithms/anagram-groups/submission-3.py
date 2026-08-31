class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        group_dict = {}

        for s in strs:
            key = ''.join(sorted(s))
            if key in group_dict:
                group_dict[key].append(s)
            else:
                group_dict[key] = [s]
        
        res = []
        for value in group_dict.values():
            res.append(value)
        
        return res