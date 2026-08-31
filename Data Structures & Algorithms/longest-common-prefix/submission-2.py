class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        sorted_strs = sorted(strs)
        print(f'sorted_strs: {sorted_strs}')

        first = sorted_strs[0]
        last = sorted_strs[-1]

        ans = 0
        for i in range(0, len(first)):
            if first[i] == last[i]:
                ans += 1
            else:
                return first[:ans]
        
        return sorted_strs[0]