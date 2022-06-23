num_map={"2":['a','b','c'],
                "3":['d','e','f'],
                 "4":['g','h','i'],
                 "5":['j','k','l'],
                 "6":['m','n','o'],
                 "7":['p','q','r','s'],
                 "8":['t','u','v'],
                 "9":['w','x','y','z']
                }

def solve(num,ans,cur,i):
    if len(cur)==len(num):
        ans.append(cur)
        return
    
    lst=num_map[num[i]]
    
    for ch in lst:
        cur=cur+ch
        solve(num,ans,cur,i+1)
        cur=cur[:len(cur)-1]
    return
    
        
        


class Solution:
    def letterCombinations(self, num: str) -> List[str]:
        
        ans=[]
        cur=""
        solve(num,ans,cur,0)
        return ans if num!="" else []