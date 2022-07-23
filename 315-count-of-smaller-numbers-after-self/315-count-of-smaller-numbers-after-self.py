class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        
        n=len(nums)
        out=[0 for i in range(n)]
        
        def sort(arr):
            
            if len(arr)>1:
                mid=len(arr)//2
                left,right=sort(arr[:mid]),sort(arr[mid:])
                i=0
                j=0
                ans=[]
                leftmore=0
                while i<mid and j<len(right):
                    if left[i][1]<=right[j][1]:
                        ans.append(left[i])
                        out[left[i][0]]+=leftmore
                        i+=1
                    else:
                        ans.append(right[j])
                        leftmore+=1
                        j+=1

                while j<len(right):
                    ans.append(right[j])
                    leftmore+=1
                    j+=1
                while i<len(left):
                    ans.append(left[i])
                    out[left[i][0]]+=leftmore
                    i+=1

                return ans
            
            return arr

        
        nums=sort(list(enumerate(nums)))
        
        # print(nums)
        return out