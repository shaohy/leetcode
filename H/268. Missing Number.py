class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_list = sorted(nums)
        for i in range(len(num_list)):
            if i != num_list[i]:
                return i
        return len(num_list)

