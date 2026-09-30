class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        grouped_strs = {}

        for word in strs:
            sorted_key = ''.join(sorted(word))

            if sorted_key in grouped_strs:
                grouped_strs[sorted_key].append(word)
            else:
                grouped_strs[sorted_key] = [word]
        
        return [x for x in grouped_strs.values()]
