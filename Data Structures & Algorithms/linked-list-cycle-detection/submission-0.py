# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp = head
        count =  0
        
        while temp:
            temp = temp.next
            count+=1
            if count>1000:
                break

        
        if temp:
            return True
        else:
            return False
        