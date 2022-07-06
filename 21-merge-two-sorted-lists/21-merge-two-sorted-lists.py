# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if not list1:
            return list2
        
        if not list2:
            return list1
        
        
        p1=list1
        p2=list2
        prev=None
        while p1 and p2:
            
            while p1 and p1.val<=p2.val:
                prev=p1
                p1=p1.next
            if prev:
                prev.next=p2
            p1,p2=p2,p1
            
        if list1.val<=list2.val:
            return list1
        else:
            return list2
            
                
        
        