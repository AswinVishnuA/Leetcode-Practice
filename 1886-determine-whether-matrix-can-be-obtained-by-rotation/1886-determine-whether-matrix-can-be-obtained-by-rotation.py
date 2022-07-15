class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        
        temp=mat
        
        d=True
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j]!=target[i][j]:
                    d=False
        if d:
            return d
        
        temp=mat[::-1]
        
        for i in range(len(temp)):
            for j in range(i):
                temp[i][j],temp[j][i]=temp[j][i],temp[i][j]
        a=True
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j]!=target[i][j]:
                    a=False
        
        if a:
            return a
        temp=temp[::-1]
        
        for i in range(len(temp)):
            for j in range(i):
                temp[i][j],temp[j][i]=temp[j][i],temp[i][j]
        b=True
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j]!=target[i][j]:
                    b=False
        if b:
            return b
        temp=temp[::-1]
        
        for i in range(len(temp)):
            for j in range(i):
                temp[i][j],temp[j][i]=temp[j][i],temp[i][j]
        c=True
        for i in range(len(temp)):
            for j in range(len(temp[0])):
                if temp[i][j]!=target[i][j]:
                    c=False
        if c:
            return c
        
        return False
        