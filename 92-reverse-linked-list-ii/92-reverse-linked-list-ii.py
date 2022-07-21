# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        temp=head
        prev=None
        i=1
        while temp and i<left:
            prev=temp
            temp=temp.next
            i+=1
        
#         temp2=temp
#         while temp2 and i<=right:
#             temp2=temp2.next
#             i+=1
        
        i=left
        prev2=None
        temp2=temp
        while temp and i<=right:
            nextn=temp.next
            temp.next=prev2
            prev2=temp
            temp=nextn
            i+=1
        
        temp2.next=temp

        if prev:
            prev.next=prev2
            return head
        else:
            return prev2
            
        
        
            
        
            
            
            
        