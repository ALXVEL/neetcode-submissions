class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
    
        Left = 1
        Right = max(piles)


        while Left <= Right:
            mid = (Right + Left) // 2

            hoursEaten = 0
            for pile in piles:
                hoursEaten += math.ceil(pile / mid)

            # Koko eats it too fast
            if hoursEaten <= h:
                Right = mid - 1
            # Koko eats it too slow
            else:
                Left = mid + 1
        
        return Left
