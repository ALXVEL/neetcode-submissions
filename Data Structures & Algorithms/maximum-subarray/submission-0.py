class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = float('-inf')
        maxSum = currSum
        L = 0

        for R in range(len(nums)):
            if currSum < 0:
                L = R
                currSum = 0

            currSum += nums[R]
            
            if currSum > maxSum:
                maxSum = currSum

        return maxSum