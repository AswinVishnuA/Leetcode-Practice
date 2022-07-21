# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        cur=head
        prev=None
        i=1
        while cur and i<left:
            prev=cur
            cur=cur.next
            i+=1
        
        i=left
        prev2=None
        temp=cur
        while cur and i<=right:
            nextn=cur.next
            cur.next=prev2
            prev2=cur
            cur=nextn
            i+=1
        
        temp.next=cur

        if prev:
            prev.next=prev2
            return head
        else:
            return prev2
            
        
        
            
        
            
            
            
        