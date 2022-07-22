# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head==None:
            return None
        
        prevl=None
        prevg=None
        lhead=None
        ghead=None
        cur=head
        while cur:
            if cur.val<x:
                if prevl==None:
                    prevl=cur
                    lhead=prevl
                else:
                    prevl.next=cur
                    prevl=cur
            else:
                if prevg==None:
                    prevg=cur
                    ghead=prevg
                else:
                    prevg.next=cur
                    prevg=cur
            cur=cur.next
        
        if lhead and ghead:
            prevl.next=ghead
            prevg.next=None
            return lhead
        
        if lhead:
            return lhead
        
        if ghead:
            return ghead
        
        
            
        