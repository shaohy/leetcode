class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        new_list = []
        for i in A:
            new_list.append((abs(i)) ** 2)
        new_list.sort()
        a = sorted([abs(i) ** 2 for i in A])
        return new_list
