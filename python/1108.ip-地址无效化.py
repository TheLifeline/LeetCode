#
# @lc app=leetcode.cn id=1108 lang=python3
#
# [1108] IP 地址无效化
#

# @lc code=start
class Solution:
	def defangIPaddr(self, address: str) -> str:
		result=""
		for ch in address:
			if ch ==".":
				result+="[.]"
			else:
				result+=ch
		return result
# @lc code=end

