#
# @lc app=leetcode.cn id=83 lang=python3
#
# [83] 删除排序链表中的重复元素
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
	def deleteDuplicates(self, head: ListNode) -> ListNode:
		p=head
		p1=head
		if p is None:
			return p
		while(True):
			p1=p1.next
			if p1 is None:
				break
			elif p1.val==p.val:
				p.next=p1.next
				p1.next = None
				p1=p
			else:
				p=p1
		return head

# @lc code=end

