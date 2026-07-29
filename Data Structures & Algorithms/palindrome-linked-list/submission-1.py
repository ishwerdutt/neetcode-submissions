# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # emp_list =  []
        # temp = head

        # while temp:
        #     emp_list.append(temp.val)
        #     temp = temp.next
        # if emp_list == emp_list[::-1]:
        #     return True
        # else:
        #     return False
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second = slow.next
        print(head.val)
        slow.next = None



        prev, curr = None, second

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        temp1 = head
        temp2 = prev

        while temp1 and temp2:
            if temp1.val == temp2.val:
                temp1 = temp1.next
                temp2 = temp2.next
            else:
                return False
        return True


                
        