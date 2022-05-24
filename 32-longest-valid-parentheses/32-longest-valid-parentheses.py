class Solution:
    def longestValidParentheses(self, s: str) -> int:
        arr=[]
        n=len(s)
        ans=0

        for i in range(n):
            if s[i] == "(":
                arr.append(i)
            else:
                if len(arr)!=0:
                    if s[arr[len(arr)-1]]=="(":
                        arr.pop()
                    else:
                        arr.append(i)
                else:
                    arr.append(i)
        if len(arr)==0:
            ans=n
        else:
            b=n
            a=0
            while(len(arr)!=0):
                a = arr.pop()
                ans=max(ans,b-a-1)
                b=a
            ans=max(ans,b)
        
        return ans