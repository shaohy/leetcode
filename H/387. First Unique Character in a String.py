# class Solution:
#     def firstUniqChar(self, s: str) -> int:
#         list = []
#         for i in range(len(s)):
#             if s.count(s[i]) == 1:
#                 list.append(i)
#
#         if not list:
#             return -1
#         else:
#             return list[0]

class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_dict = {}
        for i in range(len(s)):
            if s[i] not in char_dict:
                char_dict[s[i]] = [i, 1]
                continue
            char_dict[s[i]][1] += 1
        for k, v in char_dict.items():
            if v[1] == 1:
                return v[0]
        return -1