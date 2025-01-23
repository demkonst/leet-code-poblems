class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False

        digits = []

        while x >= 10:
            digits.append(x % 10)
            x = x // 10

        digits.append(x)

        for i, x in enumerate(digits):
            if x != digits[len(digits) - i - 1]:
                return False

        return True


s = Solution()
print(s.isPalindrome(-121))
print(s.isPalindrome(121))
print(s.isPalindrome(0))
print(s.isPalindrome(1))
print(s.isPalindrome(10))
print(s.isPalindrome(1221))
print(s.isPalindrome(1223))
