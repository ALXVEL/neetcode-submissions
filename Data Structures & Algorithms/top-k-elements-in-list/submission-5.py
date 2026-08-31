class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        buckets = [[] for _ in range(0, len(nums)+1)]

        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1
        
        for key, value in count.items():
            buckets[value].append(key)
        
        print(buckets)

        ans = []
        for bucket in reversed(buckets):
            ans.extend(bucket)
        
        return ans[:k]
