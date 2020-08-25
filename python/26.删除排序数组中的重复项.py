#
# @lc app=leetcode.cn id=26 lang=python3
#
# [26] 删除排序数组中的重复项
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        start=0
        end=0
        all_len=len(nums)
        if all_len==0:
            return 0
        while(True):
            list_len=end-start
            end+=1
            if end==all_len:
                break
            if nums[end]>nums[start]:
                nums[start+1]=nums[end]# 注意这里如果用循环将元素一个一个向前移的话，会超时。
                start+=1
        return start + 1
# @lc code=end

