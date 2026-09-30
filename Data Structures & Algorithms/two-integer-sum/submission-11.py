class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        check = {}

        for i in range(0, len(nums)):
            diff = target - nums[i]

            if diff in check:
                return [check[diff], i]
            else:
                check[nums[i]] = i
        
        return [0,0]