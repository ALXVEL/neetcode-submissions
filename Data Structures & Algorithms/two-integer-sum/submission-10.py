class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # key == value
        # value = index
        track = {}  

        ans = []

        for key, value in enumerate(nums):
            diff = target - value
            if diff in track:
                return [track[diff], key]

            track[value] = key

        return [0,0] 

