class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # key == sorted str
        # value = list of strs
        track = {}

        for word in strs:
            sorted_word = ''.join(sorted(word))

            if sorted_word in track:
                track[sorted_word].append(word)
            else:
                track[sorted_word] = [word]
        
        # go through the tracking
        ans = []

        for value in track.values():
            ans.append(value)
    
        return ans
