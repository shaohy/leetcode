class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums_list = []
        for i in nums1:
            if i in nums2:
                nums_list.append(i)
                nums2.remove(i)
        return nums_list

