# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        pos = 1
        lenofll = 0
        temp = head
        while temp:
            lenofll+=1
            temp = temp.next
            
        if lenofll==n:
            return head.next
        
        temp2= head
        
        for _ in range(lenofll-n-1):
            temp2 = temp2.next

        temp2.next = temp2.next.next
        return head

        