#
# @lc app=leetcode.cn id=1047 lang=python3
#
# [1047] 删除字符串中的所有相邻重复项
#

# @lc code=start
class Solution:
	def removeDuplicates(self, S: str) -> str:
		result=[]
		for ch in S:
			if len(result)==0:
				result.append(ch)
			else:
				temp=result.pop()
				if temp!=ch:
					result.append(temp)
					result.append(ch)
		return "".join(result)

        
# @lc code=end

