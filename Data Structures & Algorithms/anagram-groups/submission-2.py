class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams_map = {}

        for anagram in strs:
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram in anagrams_map:
                anagrams_map[sorted_anagram].append(anagram)
            else:
                anagrams_map[sorted_anagram] = [anagram]
        
        result = []
        for key, value in anagrams_map.items():
            result.append(value)
        
        return result