from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        n2 = n * n
        expected_sum = (n2 + 1) * n2 / 2

        sum = 0
        for row in grid:
            for cell in row:
                sum += cell

        return []



s = Solution()
print(s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]]))