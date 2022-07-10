class Solution:
    def canChange(self, start: str, target: str) -> bool:
        
        length=len(start)
        
        sarr=[]
        tarr=[]
        A=""
        B=""
        for i in range(length):
            
            if start[i]=="L" or start[i]=="R":
                sarr.append(i)
                A+=start[i]
            
            if target[i]=="L" or target[i]=="R":
                tarr.append(i)
                B+=target[i]
        
        if len(A)!=len(B):
            return False
            
        for i in range(len(sarr)):
            
            if (A[i]=="L" and B[i]=="R") or (A[i]=="L" and sarr[i]<tarr[i]):
                return False
            elif (A[i]=="R" and B[i]=="L") or (A[i]=="R" and sarr[i]>tarr[i]):
                return False
        
        # print(sarr,tarr)
        
        return True