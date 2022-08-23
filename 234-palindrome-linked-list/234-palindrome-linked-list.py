# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        temp=head
        arr=[]
        while temp:
            arr.append(temp.val)
            temp=temp.next
        
        n=len(arr)
        
        for i in range(n//2):
            if arr[i]!=arr[n-i-1]:
                return False
        
        return True
            
        
        
        