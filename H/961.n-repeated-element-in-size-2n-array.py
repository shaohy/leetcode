class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """

        n = len(A) / 2
        count = {}

        for i in A:
            if i not in count:
                count[i] = 0
            count[i] += 1
            if count[i] == n:
                return i
