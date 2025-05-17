from typing import List


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        s1 = []
        s2 = []

        for i in range(len(nums)):
            s1.append(nums[nums[i]])
            if nums[i] < i:
                s2.append(nums[] + i)
            s2.append(nums[] + i)
        return []


solution = Solution()
s1 = solution.buildArray([0, 2, 1, 5, 3, 4])
