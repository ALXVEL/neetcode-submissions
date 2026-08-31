class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        Left, Right = 0, len(numbers) - 1

        while Left < Right:
            if numbers[Left] + numbers[Right] == target:
                return [Left+1, Right+1]
            elif numbers[Left] + numbers[Right] < target:
                Left+=1
            else:
                Right-=1
        
        return [Left+1,Right+1]