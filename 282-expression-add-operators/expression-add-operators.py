class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:

        n=len(num)
        ans=[]
        def dfs(idx,path,curr,prev):
            
            if idx==n:
                if curr==target:
                    ans.append(path)
                return
            
            for i in range(idx,n):
                if idx!=i and num[idx]=="0":
                    break
                st=num[idx:i+1]
                val=int(st)

                if idx==0:
                    dfs(i+1,st,val,val)
                else:
                    dfs(i+1,path+"+"+st,curr+val,val)
                    dfs(i+1,path+"-"+st,curr-val,-val)
                    dfs(i+1,path+"*"+st,curr-prev + (prev*val),prev*val)


        dfs(0,"",0,0)
        return ans
        

        