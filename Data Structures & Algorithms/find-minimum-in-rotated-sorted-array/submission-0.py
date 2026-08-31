class Solution:
    def findMin(self, nums: List[int]) -> int:

        Left, Right = 0, len(nums) - 1

        while Left <= Right:
            mid = (Left + Right) // 2
            print(nums[mid])

            if nums[mid] < nums[Right]:
                Right = mid
            else:
                Left = mid + 1
        
        return nums[mid]