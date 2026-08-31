class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sums_map = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]
            
            if diff in sums_map.keys():
                return [sums_map[diff],i ]
            else:
                sums_map[nums[i]] = i
        
        return [0,0]

