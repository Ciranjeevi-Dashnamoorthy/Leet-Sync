class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        """
        Observation
        
        """

        d={}
        if len(s1)+len(s2)!=len(s3):
            return False
        def dfs(i,j):

            if i+j==len(s1)+len(s2):
                return True
            
            if (i,j) in d:
                return d[(i,j)]
            
            if i<len(s1) and s1[i]==s3[i+j] and dfs(i+1,j):
                d[(i,j)]=True
               
                return True
            
            if j<len(s2) and s2[j]==s3[i+j] and dfs(i,j+1):
                d[(i,j)]=True
            
                return True
            
            d[(i,j)]=False
            return False

        return dfs(0,0)
        
        

        
        