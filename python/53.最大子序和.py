#
# @lc app=leetcode.cn id=53 lang=python3
#
# [53] 最大子序和
# 这个是典型的分治问题

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = nums[0]
        m=0
        for num in nums:
            m=num+m
            if m<num:
                m=num
            if m>max_:
                max_ = m
        return max_
            
# @lc code=end

