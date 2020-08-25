#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#

# @lc code=start
class Solution:
	def addBinary(self, a: str, b: str) -> str:
		result=""
		if len(a)>len(b):
			for i in range(len(a)-len(b)):
				b='0'+b
		else:
			for i in range(len(b)-len(a)):
				a='0'+a
		la=list(a)
		lb=list(b)
		flag=False
		while(True):
			if len(la)==0:
				break
			flag,r=self.add_ch(la.pop(),lb.pop(),flag)
			result=r+result
		if flag:
			result='1'+result
		return result

	def add_ch(self,ch1,ch2,flag):
		r=''
		rflag=False
		if ch1=='1' and ch2=='1':
			r='0'
			rflag=True
		elif ch1=='1' and ch2=='0':
			r='1'
		elif ch1=='0' and ch2=='1':
			r='1'
		elif ch1=='0' and ch2=='0':
			r='0'
		if flag and r=='0':
			r='1'
		elif  flag and r=='1':
			r='0'
			rflag=True
		elif flag==False and r=='0':
			r='0'
		elif  flag==False and r=='1':
			r='1'
		return rflag,r
# @lc code=end

