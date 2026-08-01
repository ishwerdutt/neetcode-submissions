# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr=slow.next

        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        temp1=head
        temp2=prev
        twin_sum=[]

        while temp1 and temp2:
            twin_sum.append(temp1.val+temp2.val)
            temp1=temp1.next
            temp2=temp2.next

        return max(twin_sum)
            


        
