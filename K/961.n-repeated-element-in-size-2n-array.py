class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        while 1:
            s = random.sample(A, 2)
            if s[0] == s[1]:
                return s[0]
