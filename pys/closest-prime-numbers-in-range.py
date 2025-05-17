from typing import List, Dict


class Solution:
    def closest_primes(self, left: int, right: int) -> List[int]:
        num1 = -1
        num2 = -1

        primes = self.prime_numbers(right)
        primes = [prime for prime in primes if left <= prime <= right]

        diff = right - left + 1
        for i in range(len(primes) - 1):
            x = primes[i]
            y = primes[i + 1]
            new_diff = y - x

            if 0 < new_diff < diff:
                diff = new_diff
                num1 = x
                num2 = y

        if num1 == num2:
            return [-1, -1]
        else:
            return [num1, num2]

    def prime_numbers(self, n: int) -> list[int]:
        primes = {i: True for i in range(2, n + 1)}

        for i in range(2, n + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False

        return [key for key, value in primes.items() if primes[key]]


s = Solution()
# print(s.closest_primes(10, 19))
# print(s.closest_primes(4, 6))
# print(s.closest_primes(19, 31))
print(s.closest_primes(710119, 710189))
