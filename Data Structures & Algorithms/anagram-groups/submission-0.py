class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        this_dict = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            if sorted_word in this_dict:
                this_dict[sorted_word].append(word)
            else:
                this_dict[sorted_word] = []
                this_dict[sorted_word].append(word)
        
        res = []
        for n in this_dict.values():
            res.append(n)
        
        return res