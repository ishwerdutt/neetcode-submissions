# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        temp = head
        n = 0
        while temp:
            n+=1
            temp=temp.next
            


        twins = []
        temp1=head
        for i in range(int(n/2)):
            
            temp2 = head
            for _ in range(n-1-i):
                temp2=temp2.next
            twins.append([temp1.val, temp2.val])
            temp1=temp1.next
            

        twins_sum = [num[0]+num[1] for num in twins]
        
        return max(twins_sum)
