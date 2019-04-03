class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            "I":
                1,
            "V":
                5,
            "X":
                10,
            "L":
                50,
            "C":
                100,
            "D":
                500,
            "M":
                1000
        }
        # output = 0
        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        # for i in s:
        #     output += dic[i]
        # return output
        prev = 0
        for i in s:
            cur = dic[i]


class Solution:
    def romanToInt(self, s):
        romanToInt_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        count = 0
        prev = float("inf")
        cur = 0
        for c in s:
            cur = romanToInt_dict[c]
            if cur > prev:
                count -= 2 * prev
            count += cur
            prev = cur

        return count
