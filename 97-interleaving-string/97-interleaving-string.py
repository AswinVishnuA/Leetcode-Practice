class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        @lru_cache(None)
        def solve(str1,str2,str3):
            # print(str1,str2,str3)
            if len(str1)+len(str2)!=len(str3):
                return False

            if str1=="" and str2=="" and str3=="":
                return True
            if str1=="" and str2!="":
                if str2==str3:
                    return True
                else:
                    return False
            if str1!="" and str2=="":
                if str1==str3:
                    return True
                else:
                    return False
                    
            i=0
            j=0
            k=0
            ans=0
            while(k<len(str3)):

                if i<len(str1) and j<len(str2) and k<len(str3) and str1[i]==str2[j]==str3[k]:
                    # print(str1[i+1:],str2[j:],str3[k+1:],"|",str1[i:],str2[j+1:],str3[k+1:])
                    return solve(str1[i+1:],str2[j:],str3[k+1:]) or solve(str1[i:],str2[j+1:],str3[k+1:])
                    
                
                elif i<len(str1)  and k<len(str3) and str1[i]==str3[k]:
                    i+=1
                    k+=1
                elif j<len(str2) and k<len(str3) and str2[j]==str3[k]:
                    j+=1
                    k+=1
                else:
                    # print(False)
                    return False
            # print(i,j,k)
            ans=ans or (i+j==k and k==len(str3))
            # print(ans)
            return ans
        
        return solve(s1,s2,s3)
        