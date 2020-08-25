#
# @lc app=leetcode.cn id=27 lang=python3
#
# [27] 移除元素
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        start=-1
        end=-1
        all_len=len(nums)
        if all_len==0:
            return 0
        while(True):
            list_len=end-start
            end+=1
            if end==all_len:
                break
            if nums[end]!=val:
                nums[start+1]=nums[end]
                start+=1
        return start + 1
# @lc code=end

