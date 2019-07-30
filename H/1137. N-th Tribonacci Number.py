class Solution:
    def tribonacci(self, n: int) -> int:
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1
        elif n > 2:
            return self.tribonacci(n - 3) + self.tribonacci(n - 2) + self.tribonacci(n - 1)
        tribonacci_numbers = {0: 0, 1: 1, 2: 1}
        for i in range(3, n + 1):
            tribonacci_numbers[i] = tribonacci_numbers[i - 3] + tribonacci_numbers[i - 2] + tribonacci_numbers[i - 1]
        return tribonacci_numbers[n]
