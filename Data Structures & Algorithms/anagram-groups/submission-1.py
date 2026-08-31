class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = {}

        for word in strs:

            sorted_word = sorted(word)
            sorted_word = "".join(sorted_word)

            if sorted_word in res:
                res[sorted_word].append(word)
            else:
                res[sorted_word] = [word]
        
        ans = []
        for key, value in res.items():
            ans.append(value)
        
        return ans