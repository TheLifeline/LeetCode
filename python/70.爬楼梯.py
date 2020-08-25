#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
	def climbStairs(self, n: int) -> int:
		l=[]
		for i in range(n+2):
			if i==0:
				l.append(i)
			elif i==1:
				l.append(i)
			else:
				l.append(l[i-1]+l[i-2])
		return l[n+1]
# @lc code=end

