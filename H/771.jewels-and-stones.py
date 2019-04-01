class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        output = 0
        for i in J:
            if i in S:
                output += 1
