#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		#这个实现看起来更优雅一些。。。。
        temp_num = 0
        for num in digits:
            temp_num=temp_num*10+num
        temp_num+=1
        result = []
        while temp_num>0:
            result.insert(0,temp_num%10)
            temp_num=temp_num//10
        return result
		

        
# @lc code=end

