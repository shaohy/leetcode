class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        even_output = []
        odd_output = []
        for i in A:
            if i % 2 == 0:
                even_output.append(i)
            else:
                odd_output.append(i)
        return even_output + odd_output