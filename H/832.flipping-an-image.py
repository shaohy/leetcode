class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # flipping_list = []
        # invert_list = []
        # for i in A:
        #     flipping_list += i[::-1]
        # for i in flipping_list:
        #     for j in i:
        #         if j == 0:
        #             invert_list.append(1)
        #         if j == 1:
        #             invert_list.append(0)
        # return invert_list

        return [[int(not b) for b in a[::-1]] for a in A]
