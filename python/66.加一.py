#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#

# @lc code=start
class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		num=0
		for n in digits:
			num=num*10+n
		num+=1
		l=[]
		while(True):
			if num==0:
				break
			else:
				l.append(num%10)
				num=num//10
		return l[::-1]
		

        
# @lc code=end

