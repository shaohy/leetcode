class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for i in nums:
            dic[i] = nums.count(i)
        for k,v in dic:
            if dic.values() > (len(nums)/2):
                return dic.keys()
