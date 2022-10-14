# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        n=0
        
        temp=head
        
        while temp:
            temp=temp.next
            n+=1
        
        temp=head
        prev=None
        i=0
        while temp:
            if i== n//2:
                if i==0:
                    return None
                prev.next=temp.next
                return head
            prev=temp
            temp = temp.next
            i+=1
        
        return None
        