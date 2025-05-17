from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        _0 = 0
        _1 = 0
        _2 = 0
        for x in nums:
            if x == 0:
                _0 += 1
            elif x == 1:
                _1 += 1
            else:
                _2 += 1

        for i in range(len(nums)):
            if _0 > 0:
                nums[i] = 0
                _0 -= 1
            elif _1 > 0:
                nums[i] = 1
                _1 -= 1
            else:
                nums[i] = 2


def test_1():
    s = Solution()
    nums = [2, 0, 2, 1, 1, 0]
    s.sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]


def test_2():
    s = Solution()
    nums = [2, 0, 1]
    s.sortColors(nums)
    assert nums == [0, 1, 2]
