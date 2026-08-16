# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        l = 1
        temp = head

        if not head:
            return 

        while temp and temp.next:
            l+=1
            temp = temp.next
        

        temp.next = head

        effective_rot = k%l
        wanted_tail = l-effective_rot

        while wanted_tail>0:
            temp = temp.next
            wanted_tail-=1
        
        new_head = temp.next
        temp.next = None
        return new_head
        

    

        