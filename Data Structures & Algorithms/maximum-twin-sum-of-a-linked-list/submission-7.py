# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        

        # what we will do is reverse the next half of the linked List and then we will parallaly traverse the both of the lists and find the max sum.
        slow = head
        fast = head.next.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev = None
        curr = slow.next

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        temp1 = prev
        temp2 = head

        twins_sum = []

        while temp1 and temp2:
            twins_sum.append(temp1.val+temp2.val)
            temp1 = temp1.next
            temp2 = temp2.next

        maximum = float('-inf')

        for num in twins_sum:
            if num>maximum:
                maximum = num
        return maximum        