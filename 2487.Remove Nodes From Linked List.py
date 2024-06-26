# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        stack=[]
        while head:
            curval = head.val
            while stack and stack[-1] < curval:
                stack.pop()
            stack.append(head.val)
            head = head.next
        head = ListNode()
        tmp1 = head
        i=0
        l=len(stack)
        while i<l:
            tmp = ListNode()
            tmp.val = stack[i]
            head.next = tmp
            head = head.next
            i+=1
        tmp1=tmp1.next
        return tmp1
