class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def BinarySearch(arr, target):
            low, high = 0, len(arr) - 1

            while low <= high:
                mid = (low+high) // 2
                if arr[mid] < target:
                    low = mid + 1
                elif arr[mid] > target:
                    high = mid - 1
                else:
                    return mid
            
            return -1 

        for row in matrix:
            ans = BinarySearch(row, target)
            if ans != -1:
                return True

        return False