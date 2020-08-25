#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
	def lengthOfLastWord(self, s: str) -> int:
		count=0
		block=0
		for ch in s[::-1]:
			if ch==" ":
				block+=1
			else: 
				break
		for ch in s[0:len(s)-block]:
			if ch == ' ':
				count=0
			else:
				count+=1
		return count
		
        
# @lc code=end

