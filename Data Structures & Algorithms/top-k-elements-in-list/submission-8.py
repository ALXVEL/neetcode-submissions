class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # first we can make a count
        count = {}
        for i in range(0, len(nums)):
            count[nums[i]] = count.get(nums[i], 0) + 1
        
        # now we create a bucket list
        buckets = [[] for _ in range(0, len(nums) + 1)]

        # we put the counts into buckets
        for key, value in count.items():
            buckets[value].append(key)
        
        # normalize the buckets
        ans = []
        for bucket in buckets:
            ans.extend(bucket)
        
        return ans[-k:]
