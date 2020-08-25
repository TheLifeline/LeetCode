#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
# 这题可以二分查找，好像也可以顺序查找，我先试一下顺序查找可不可以，可能会卡时间？
# 惊了，顺序查找竟然没卡时间。主要是边界卡了一下。

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i]>=target:
                return i
        return len(nums)
            
        
# @lc code=end

