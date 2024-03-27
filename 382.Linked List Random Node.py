# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    currPointer=None
    stack=None
    counter =0 
    def __init__(self, head: Optional[ListNode]):
        self.stack = head
        self.currPointer = head
        self.counter = 0
        while self.currPointer:
            self.counter += 1
            self.currPointer = self.currPointer.next

    def getRandom(self) -> int:
        n=random.uniform(0,self.counter)
        self.currPointer = self.stack
        while n>1:
            self.currPointer = self.currPointer.next
            n-=1
        return self.currPointer.val
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()
