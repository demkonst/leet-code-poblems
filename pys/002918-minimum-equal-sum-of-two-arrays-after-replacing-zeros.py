from typing import List


class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        (sum1, zeros1) = self.get_sum(nums1)
        (sum2, zeros2) = self.get_sum(nums2)

        result1 = sum1 + zeros1
        result2 = sum2 + zeros2

        if zeros1 == 0 and sum2 + zeros2 > sum1:
            return -1

        if zeros2 == 0 and sum1 + zeros1 > sum2:
            return -1

        return max(sum1 + zeros1, sum2 + zeros2)

    def get_sum(self, nums: List[int]) -> (int, int):
        total_sum = 0
        zeros = 0

        for i in range(len(nums)):
            total_sum += nums[i]

            if nums[i] == 0:
                zeros += 1

        return total_sum, zeros


s = Solution()
print(s.minSum([0], [0]))
print(s.minSum([0, 0, 0], [0, 0]))
print(s.minSum([1], [1]))
print(s.minSum([3, 2, 0, 1, 0], [3, 2, 0, 1, 0]))
print(s.minSum([3, 2, 0, 1, 0], [6, 5, 0]))
print(s.minSum([2, 0, 2, 0], [1, 4]))
print(s.minSum([2, 0, 2, 0], [2, 0, 2, 0, 0]))
print(s.minSum([2, 0, 2, 1], [6]))
