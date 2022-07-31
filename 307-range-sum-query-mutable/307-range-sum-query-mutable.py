class Node:
    
    def __init__(self,l,r):
        self.start=l
        self.end=r
        self.total=0
        self.left=None
        self.right=None
    

class NumArray:

    def __init__(self, nums: List[int]):
        n=len(nums)
        self.n=n
        def create(l,r):
            
            if l>r:
                return None
            
            if l==r:
                node=Node(l,r)
                node.total=nums[l]
                return node
            
            mid=(l+r)//2
            
            node=Node(l,r)
            node.left=create(l,mid)
            node.right=create(mid+1,r)
            
            node.total=node.left.total+node.right.total
            
            return node
            
        
        
        self.root=create(0,n-1)
        

    def update(self, index: int, val: int) -> None:
        
        
        def search(cur):
            
            if not cur:
                return cur
            
            if cur.left==None and cur.right==None:
                cur.total=val
                return cur
                
            
            mid=(cur.start + cur.end)//2
            
            if mid>=index:
                cur.left=search(cur.left)
            else:
                cur.right=search(cur.right)
            
            cur.total=cur.left.total+cur.right.total
            
            return cur
        
        self.root=search(self.root)
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        
        def getsum(cur,l,r):
            
            
            if cur.start==l and cur.end==r:
                return cur.total
            
            mid=(cur.start + cur.end)//2
            
            if r<=mid:
                return getsum(cur.left,l,r)
            elif l>mid:
                return getsum(cur.right,l,r)
            else:
                return getsum(cur.left,l,mid)+getsum(cur.right,mid+1,r)
                

            
            
            
        
        
        return getsum(self.root,left,right)
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)