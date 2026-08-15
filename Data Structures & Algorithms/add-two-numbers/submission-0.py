# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #two non empty linked lists
        num1 = ""
        num2 = ""
        n1 = 0
        n2 = 0
        temp1 = l1
        temp2 = l2

        while temp1:
            n1+=1
            temp1 = temp1.next

        while temp2:
            n2+=1
            temp2 = temp2.next

        temp1 = l1
        for _ in range(n1):
            num1 += str(temp1.val)
            temp1 = temp1.next
        temp2 = l2
        for _ in range(n2):
            num2 += str(temp2.val)
            temp2 = temp2.next
        

        num1 = num1[::-1]
        num2 = num2[::-1]

        print(num1)
        print(num2)

        ans = int(num1) + int(num2)
        ans = str(ans)[::-1]
        print(ans)

        head = None
        tail = None

        for ch in ans:
            new_node = ListNode(int(ch))
            
           

            if head is None:
                head = new_node
                tail = new_node
            else:
                tail.next = new_node
                tail = new_node

        return head

        

        




    

        