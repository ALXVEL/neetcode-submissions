class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(nums)
        print(nums)
        curr = 1
        res = 1
        for i in range(0, len(nums)):
            if i > 0:
                if nums[i] - nums[i-1] == 1:
                    print(f'{nums[i]} - {nums[i-1]}')
                    curr +=1
                elif nums[i] - nums[i-1] == 0:
                    continue
                else:
                    curr = 1
            res = max(res, curr)

        if not nums:
            return 0

        return res