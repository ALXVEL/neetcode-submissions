class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        Left, Right = 0, len(nums) - 1
        
        while Left <= Right:
            mid = (Left + Right) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] >= nums[Left]:
                # left side is sorted
                if nums[Left] <= target < nums[mid]:
                    # target is on left side (sorted)
                    Right = mid - 1
                else:
                    # recheck using the right side this time
                    Left = mid + 1
            else:
                # right side is sorted
                if nums[mid] < target <= nums[Right]:
                    # target is on right side  
                    Left = mid + 1
                else:
                    # recheck using the left side this time
                    Right = mid - 1

        return -1