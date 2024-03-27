# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        begin = head
        prev = head
        if head:
            head = head.next
        else:
            return head
        while head:
            temp = head.next
            head.next = None
            stack.insert(0,head)
            if temp:
                head = temp.next
                prev.next =temp
                prev = temp
            else:
                head = temp
        while stack:
            prev.next = stack.pop()
            prev = prev.next
        return begin 
