class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        
        ans=[]
        changed.sort()
        
        count=Counter(changed)
        skip=Counter()
        if count[0]%2==1:
            return []
        # print(count,count[2/2])
        for val in changed:
            # print(val)

            if skip[val]!=0:
                skip[val]-=1
                continue
            if count[val/2]!=0:
                skip[val/2]+=1
                count[val/2]-=1
                count[val]-=1
                ans.append(val//2)
            elif count[val*2]!=0:
                count[val]-=1
                count[val*2]-=1
                skip[val*2]+=1
                ans.append(val)
            else:
                # print(ans)
                return []
        
        return ans
        