import bisect
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:

        """
        Observation:

        for a given grapgh with edges , we need to find the minimum edges to travel to reach the node from to b

        given the queries [l,r] --> implies that we need to reach node l to node r 

        approach:

        Run BFS for every query , find the minimum edges ran to reach the teraget edge

        TC: Q*N**2 

        optimal:

        make it sorted like

        1 8 3 4 2 

        to 

        1 2 3 4 8

        maintain index to node array

        if we sort it, then we can jump from node a to 

        node b which can be <= a+maxDiff 

        USE BIANRY SERACH TO  FIND THE MAX JUMPS IN LOGN

        after finding the maximum jumps 

        to find the number of jumps

        USE BINARY UPLIFTING WITH SPARSE TABLE STRUCTURE

        TC: nlogn ( to build sorted values ) + q logn ( to process queries in sparse table)


        """

        arr=[]
        for i in range(n):
            arr.append((nums[i],i))
        arr.sort()
        d={}
        for i in range(n):
            val,idx=arr[i]
            d[idx]=i
        
        jumps=[0]*n

        for i in range(n):
            val,idx=arr[i]
            print(val)
            ans=bisect.bisect_left(arr,(val+maxDiff,float("inf")))-1
            jumps[i]=ans
        
        log=len(bin(n))-2
        up=[jumps]

        for _ in range(1,log):
            last=up[-1]
            new=[]
            for i in range(n):
                new.append(last[last[i]])
           
            up.append(new[::])

        res=[]
        for a,b in queries:

            a=d[a]
            b=d[b]

            if a==b:
                res.append(0)
                continue
            if a>b:
                a,b=b,a
            
            curr=a
            jump=0

            for k in range(log-1,-1,-1):
                if up[k][curr]<b:
                    curr=up[k][curr]
                    jump+=2**k
                
            if jumps[curr]>=b:
                res.append(jump+1)
            else:
                res.append(-1)
        return res


            
       



        