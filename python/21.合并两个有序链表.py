#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """
    解法不够好，应该使用带有头节点的链表，还是应该声明两个头节点
    但h1和h2不必声明了，并且边界处理的也不够好。
    """
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        h1=l1
        h2=l2
        result = None
        result_tail = result
        if h1==None:
            return h2
        if h2==None:
            return h1
        while(True):
            if h1 == None or h2 == None:
                break
            else:
                if h1.val<h2.val:
                    if result!=None:
                        temp=h1
                        h1=h1.next
                        result_tail.next=temp
                        result_tail=result_tail.next
                    else:
                        result=h1
                        result_tail = result
                        h1=h1.next
                else:
                    if result!=None:
                        temp=h2
                        h2=h2.next
                        result_tail.next=temp
                        result_tail=result_tail.next
                    else:
                        result=h2
                        result_tail = result
                        h2=h2.next
        if h2!=None:
            result_tail.next=h2
        else:
            result_tail.next=h1
        return result
            

        
# @lc code=end

