class Solution:
    def totalStrength(self, nums: List[int]) -> int:

        n=len(nums)
        mod=10**9 + 7 
        left=[0]*n
        right=[0]*n
        st=[]

        for i in range(n):
            while st and nums[st[-1]]>=nums[i]:
                st.pop()
            left[i]=st[-1] if st else -1
            st.append(i)
        st=[]
        for i in range(n-1,-1,-1):
            while st and nums[st[-1]]>nums[i]:
                st.pop()
            
            right[i]=st[-1] if st else n
            st.append(i)
        
        
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]=pref[i-1]+nums[i-1]
        curr=[0]*(n+2)
        for i in range(n+1):
            curr[i+1]=(curr[i]+pref[i]) %mod
        ans=0    
        for i in range(n):
            ls=i-left[i]
            rs=right[i]-i
            lc=(curr[i+1]-curr[left[i]+1])
            rc=(curr[right[i]+1]-curr[i+1])
            total=(ls*rc-rs*lc)%mod
            ans=(ans+total*nums[i])%mod
        return ans


        