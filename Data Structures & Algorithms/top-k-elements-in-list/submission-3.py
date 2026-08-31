class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        this_dict = {}
        bucketList = [ [] for i in range(-1, len(nums))]

        for n in nums:
            if n in this_dict:
                this_dict[n] += 1
            else:
                this_dict[n] = 1
        
        for key, value in this_dict.items():
            bucketList[value].append(key)
        
        print(bucketList)

        res = []
        for i in range(len(bucketList)-1,-1,-1):
            for num in bucketList[i]:
                if not len(res) == k:
                    res.append(num)    
        
        return res