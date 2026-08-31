class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        track = {}

        for index, num in enumerate(nums):
            diff = target - num
            
            if diff in track:
                return [track[diff], index]
            
            track[num] = index
        
        return [0,0]