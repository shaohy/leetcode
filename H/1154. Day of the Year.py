class Solution:
    def dayOfYear(self, date: str) -> int:
        date = date.split("-")
        year = int(date[0])
        month = int(date[1])
        day = int(date[2])

        output = 0
        dic = {0: 0, 1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

        if year % 4 == 0 and year % 100 != 0:
            dic[2] += 1

        for i in range(month):
            output += dic[i]
            print(dic[i])
        output += day
        print()

test = Solution()
# test.dayOfYear("2019-01-09")
# test.dayOfYear("2004-03-01")
# test.dayOfYear("2009-02-10")
test.dayOfYear("1900-03-25")
