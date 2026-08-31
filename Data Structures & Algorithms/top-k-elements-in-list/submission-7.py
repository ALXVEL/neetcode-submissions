class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        
        # list of tuples
        sorted_freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)

        res = []
        for key,value in sorted_freq:
            res.append(key)
        
        return res[:k]