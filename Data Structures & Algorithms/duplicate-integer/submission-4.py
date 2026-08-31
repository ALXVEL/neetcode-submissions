class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = len(set(nums))
        if len(nums) != count:
            return True
        else:
            return False