class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        this_dict = {}
        for index, value in enumerate(nums):
            n = target - value
            if n in this_dict:
                return [this_dict[n], index]
            
            this_dict[value] = index;
        
        return null