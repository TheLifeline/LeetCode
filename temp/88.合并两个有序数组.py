#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1=m-1
        p2=n-1
        max_len = m+n-1
        while True:
            if p1==-1 or p2 ==-1:
                break
            if nums1[p1]<=nums2[p2]:
                nums1[max_len]=nums2[p2]
                p2-=1
                max_len-=1
            else:
                nums1[max_len]=nums1[p1]
                p1-=1
                max_len-=1
        if p2 >=0:
            while True:
                if p2==-1:
                    break
                nums1[max_len]=nums2[p2]
                p2-=1
                max_len-=1
# @lc code=end

