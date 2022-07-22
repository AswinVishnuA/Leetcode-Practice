# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        if head==None:
            return None
        less=[]
        greater=[]
        cur=head
        while cur:
            if cur.val<x:
                less.append(cur)
            else:
                greater.append(cur)
            cur=cur.next
        
        for i in range(len(less)-1):
            less[i].next=less[i+1]
        
        for i in range(len(greater)-1):
            greater[i].next=greater[i+1]
        
        if len(greater):
            greater[-1].next=None
        
        if len(less) and len(greater):
            less[-1].next=greater[0]
            return less[0]
        if len(less)==0:
            return greater[0]
        else:
            less[-1].next=None
            return less[0]