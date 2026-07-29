# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        emp_list =  []
        temp = head

        while temp:
            emp_list.append(temp.val)
            temp = temp.next
        if emp_list == emp_list[::-1]:
            return True
        else:
            return False
        